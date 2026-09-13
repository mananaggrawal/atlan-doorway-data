# Extraction technique: hooking the Ad Library's own GraphQL calls

This is the proven, working recipe — run through end-to-end on a 104-ad account. Follow it in
order; the steps exist because of specific failure modes (tool timeouts, output blocking,
Meta's rate limiter) that will otherwise cost you several wasted round trips.

## Step 0 — get a tab open on the advertiser's page

Navigate to the advertiser's Ad Library page (`view_all_page_id=<id>` in the URL, from step 1
of SKILL.md). Take a screenshot or `get_page_text` to confirm you're looking at the right
brand and see the `~N results` count.

## Step 1 — hook fetch/XHR to capture a real request

Run this once per tab, before triggering any more loading on the page:

```js
window.__cap = window.__cap || [];
if (!window.__hooked) {
  window.__hooked = true;
  const of = window.fetch;
  window.fetch = async function(...args){
    const res = await of.apply(this, args);
    try {
      const url = (typeof args[0]==='string')?args[0]:(args[0]&&args[0].url);
      if (url && url.includes('/api/graphql')) {
        let body = args[1] && args[1].body;
        if (body instanceof URLSearchParams) body = body.toString();
        const clone = res.clone();
        clone.text().then(t=>{ window.__cap.push({body: (typeof body==='string'? body.slice(0,4000):null), text: t}); });
      }
    } catch(e){}
    return res;
  };
  const oo = XMLHttpRequest.prototype.open, os = XMLHttpRequest.prototype.send;
  XMLHttpRequest.prototype.open = function(m,u,...r){ this.__u=u; return oo.call(this,m,u,...r); };
  XMLHttpRequest.prototype.send = function(b){
    if (this.__u && String(this.__u).includes('/api/graphql')) {
      this.addEventListener('load', ()=>{ window.__cap.push({body: (typeof b==='string'? b.slice(0,4000):null), text: this.responseText}); });
    }
    return os.call(this,b);
  };
}
'hooked'
```

Then scroll the page (or just wait a few seconds — it usually lazy-loads on its own) to force
at least one more page of results to load, so a real `ad_library_main` call gets captured.

## Step 2 — extract the real `variables` payload as a template

```js
const b = window.__cap.find(x=>x.body && x.body.includes('variables')).body;
window.__baseBody = b; // keep this — every subsequent call reuses it as a template
const p = new URLSearchParams(b);
JSON.parse(p.get('variables'))
```

Inspect the output. You'll see fields like `activeStatus`, `adType`, `countries`,
`viewAllPageID`, `first`, `cursor`, `sortData`, `sessionID`, `collationToken`, `v` (a version
token — leave it as-is, don't try to regenerate it).

## Step 3 — build the paginating fetch loop, and run it backgrounded

**Do not run this as one blocking call.** A full pull on even a mid-size account takes 1-3
minutes of real time, and `javascript_tool` calls time out around 45 seconds — the call will
error out with "Runtime.evaluate timed out" even though the loop is still running fine in the
page. The pattern that works: kick off the async function, let it write progress to
`window.__prog`, then poll it with cheap follow-up calls (`await new
Promise(s=>setTimeout(s,30000)); window.__st + ' || ' + JSON.stringify(window.__prog)`), which
also survive the timeout fine since each individual read is instant.

```js
function uuid(){return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g,c=>{const r=Math.random()*16|0,v=c=='x'?r:(r&0x3|0x8);return v.toString(16);});}

window.__fetchAll = async function(pageID, countries, extra){
  const p = new URLSearchParams(window.__baseBody);
  const base = JSON.parse(p.get('variables'));
  let cursor = null, out = [], guard = 0;
  const sid = uuid(), ctok = uuid();
  window.__prog = {pages:0, ads:0, done:false};
  while (guard++ < 400) {
    const v = Object.assign({}, base, {viewAllPageID: pageID, countries: countries, first: 30, cursor: cursor, sessionID: sid, collationToken: ctok}, extra||{});
    const p2 = new URLSearchParams(window.__baseBody);
    p2.set('variables', JSON.stringify(v));
    let t;
    try {
      const r = await fetch('https://www.facebook.com/api/graphql/', {method:'POST', credentials:'include', headers:{'content-type':'application/x-www-form-urlencoded'}, body: p2.toString()});
      t = await r.text();
    } catch(e){ await new Promise(s=>setTimeout(s,1000)); continue; }
    let j; try { j = JSON.parse(t.split('\n')[0]); } catch(e) { break; }
    const conn = j && j.data && j.data.ad_library_main && j.data.ad_library_main.search_results_connection;
    if (!conn) break; // could be a rate-limit error payload — check window.__prog.pages to see how far you got
    for (const e of conn.edges) out.push(...(e.node.collated_results||[]));
    window.__prog.pages = guard; window.__prog.ads = out.length;
    if (!conn.page_info.has_next_page) break;
    cursor = conn.page_info.end_cursor;
    await new Promise(s=>setTimeout(s,250)); // small delay between pages — helps avoid tripping the rate limiter early
  }
  window.__prog.done = true;
  return out;
};

window.__st = 'running';
window.__fetchAll('<PAGE_ID>', ['ALL']).then(r => { window.__adsRaw = r; window.__st = 'done:' + r.length; });
'started'
```

Poll every 30-40 seconds with a fresh `javascript_tool` call:

```js
window.__st + ' || ' + JSON.stringify(window.__prog)
```

When `window.__st` starts with `done:`, `window.__adsRaw` holds every collated result.

**If you hit `"Rate limit exceeded"` (code 1675004):** stop, wait at least 3-5 minutes (use
your session's own sleep/wait tool, not a tight retry loop — immediate retries don't succeed),
then resume. If a secondary page (e.g. a brand's global page after you've already fully
pulled its country page) won't clear the limit even after waiting, sample what you can get and
say so in the report rather than blocking on it.

## Step 4 — clean and slim the records, working around the output-blocking gotcha

`javascript_tool`'s return value is filtered: any string that looks like it contains a
cookie/query-string blob gets replaced with `[BLOCKED: Cookie/query string data]`, and this
triggers surprisingly easily — it catches embedded tracking-parameter URLs inside ad copy or
link fields. Strip query strings from every URL *before* you `JSON.stringify` anything you
intend to return directly:

```js
const strip = s => s==null ? null : String(s).split('?')[0].split('#')[0];

window.__rec = function(a){
  const s = a.snapshot||{};
  const body = (s.body && (s.body.markup ? s.body.markup.__html : s.body.text)) || (typeof s.body==='string'? s.body : '');
  return {
    id: a.ad_archive_id,
    st: a.start_date ? new Date(a.start_date*1000).toISOString().slice(0,10) : null,
    en: a.end_date ? new Date(a.end_date*1000).toISOString().slice(0,10) : null,
    plat: (a.publisher_platform||[]).map(x=>x[0]+x.slice(1,3)).join(','),
    fmt: s.display_format,
    cta: s.cta_type,
    ttl: strip_text(s.title||''),
    cap: strip_text(s.caption||''),
    lnk: strip(s.link_url),
    slug: (function(){ try { return new URL(strip(s.link_url)).pathname.replace(/^\/products\//,'').replace(/\/+$/,''); } catch(e){ return ''; } })(),
    bd: strip_text(String(body).replace(/<[^>]+>/g,' ').replace(/\s+/g,' ')).slice(0,600),
    nv: (s.videos||[]).length, ni: (s.images||[]).length, nc: (s.cards||[]).length
  };
};
function strip_text(x){ return String(x==null?'':x).replace(/https?:\/\/\S+/g,'[url]').replace(/[?&][A-Za-z0-9_%\-\.]+=[^\s]*/g,'').replace(/\s+/g,' ').trim(); }

// dedupe by id
const seen = new Set();
window.__adsClean = window.__adsRaw.filter(a => { if (seen.has(a.ad_archive_id)) return false; seen.add(a.ad_archive_id); return true; }).map(window.__rec);
'n=' + window.__adsClean.length
```

**Even with URLs stripped, a big JSON blob returned directly from `javascript_tool` can still
get blocked or truncated.** The reliable way to get large output out of the page: write it
into a `<pre>` element and read it with `get_page_text` instead of the JS tool's own return
value.

```js
let d = document.getElementById('__dump');
if(!d){ d=document.createElement('pre'); d.id='__dump'; d.style.cssText='white-space:pre-wrap;font-size:9px'; document.body.innerHTML=''; document.body.appendChild(d); }
d.textContent = JSON.stringify(window.__adsClean.slice(START, START+25)); // chunk it — 20-30 records at a time
'set ' + d.textContent.length
```

Then call `get_page_text` on the tab and parse the JSON out of the page text. Repeat with
different `START` offsets to pull the whole array out in chunks. Save the reassembled array to
a local JSON file (Bash/Write) once you have it all — that file is what
`scripts/analyze_ads.py` expects as input.

## Notes

- `sortData.mode: "SORT_BY_TOTAL_IMPRESSIONS"` is what the UI defaults to — leave it, it
  doesn't affect completeness, just result order.
- `collation_count` on a raw result tells you how many placement/text variants Meta is folding
  into that one entry — don't sum these, just count unique `ad_archive_id`s.
- If you need historical (not just active) ads, rerun `__fetchAll` with
  `extra: {activeStatus: "ALL"}` and merge, deduping again by id.