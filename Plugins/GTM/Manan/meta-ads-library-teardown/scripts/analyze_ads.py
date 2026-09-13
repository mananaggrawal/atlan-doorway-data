#!/usr/bin/env python3
"""
Aggregate a cleaned Meta Ad Library dump into the counts a teardown report needs.

Input: a JSON file containing a list of ad records, each shaped like the output of the
`__rec`/`__adsClean` step in references/extraction.md:

    {
      "id": "1997951357569903",
      "st": "2026-07-21",          // start date, YYYY-MM-DD
      "en": "2026-07-21" | null,   // end date, or null if still open-ended
      "plat": "FAC,INS,MES,THR",   // comma-joined platform codes
      "fmt": "VIDEO" | "DCO" | "CAROUSEL" | "IMAGE",
      "cta": "SHOP_NOW" | ...,
      "ttl": "...", "cap": "...", "bd": "...",   // title / caption / body copy
      "lnk": "https://brand.com/products/foo",   // link URL, query-stripped
      "slug": "foo",                              // last path segment, derived from lnk
      "nv": 0, "ni": 0, "nc": 2                   // video/image/card asset counts
    }

Only "id", "st", "fmt" are required for the core aggregates; everything else degrades
gracefully if missing.

Usage:
    python analyze_ads.py ads.json                  # prints a JSON summary to stdout
    python analyze_ads.py ads.json --out summary.json  # also writes it to a file
    python analyze_ads.py ads.json --pretty          # pretty-print stdout

What it computes:
    - total unique ad count
    - format_counts, cta_counts, platform_counts (single codes, not the joined combos)
    - platform_combo_counts (the joined strings as-is, useful for "which placement bundle")
    - cadence_by_date: launch count per calendar date
    - product_breakdown: per slug — total, video/dco/carousel/image split, first/last live date
    - language_flags: count of records whose title/caption/body contains non-Latin script,
      broken out by script family (Devanagari, Tamil, Telugu, Kannada, Malayalam, Bengali,
      Gurmukhi, Gujarati, Oriya, Arabic, Chinese/CJK) — a strong signal for the
      language/geography section, though always eyeball a few flagged and unflagged records
      before writing the "zero non-English creative" style claim, since transliterated
      (romanised) regional language won't be caught by script detection alone
    - repeated_hooks: titles/captions that appear on more than one distinct product slug —
      a ready-made list for the "same script across multiple SKUs" gaps-and-opportunities check
    - templated_placeholder_count: records whose title or body looks like an unfilled template
      (contains "{{" ... "}}", a common DCO catalog-feed artifact)

This script does NOT try to guess brand-specific messaging devices (loyalty program mentions,
named seasonal sales, discount codes, etc.) — those vary too much by brand to hardcode. Read
the actual copy for those, per SKILL.md step 4.
"""
import json
import re
import sys
import argparse
from collections import Counter, defaultdict

SCRIPT_RANGES = {
    "Devanagari (Hindi/Marathi)": (0x0900, 0x097F),
    "Bengali": (0x0980, 0x09FF),
    "Gurmukhi (Punjabi)": (0x0A00, 0x0A7F),
    "Gujarati": (0x0A80, 0x0AFF),
    "Oriya": (0x0B00, 0x0B7F),
    "Tamil": (0x0B80, 0x0BFF),
    "Telugu": (0x0C00, 0x0C7F),
    "Kannada": (0x0C80, 0x0CFF),
    "Malayalam": (0x0D00, 0x0D7F),
    "Arabic": (0x0600, 0x06FF),
    "CJK (Chinese/Japanese)": (0x4E00, 0x9FFF),
}


def detect_scripts(text):
    found = set()
    if not text:
        return found
    for ch in text:
        cp = ord(ch)
        for name, (lo, hi) in SCRIPT_RANGES.items():
            if lo <= cp <= hi:
                found.add(name)
    return found


def load(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise SystemExit("Input must be a JSON array of ad records.")
    return data


def analyze(ads):
    total = len(ads)
    fmt_counts = Counter()
    cta_counts = Counter()
    plat_single_counts = Counter()
    plat_combo_counts = Counter()
    cadence = Counter()
    products = defaultdict(lambda: {"n": 0, "VIDEO": 0, "DCO": 0, "CAROUSEL": 0, "IMAGE": 0,
                                     "OTHER": 0, "first": None, "last": None})
    lang_hits = defaultdict(int)
    lang_examples = defaultdict(list)
    templated = []
    hook_to_slugs = defaultdict(set)

    for a in ads:
        fmt = a.get("fmt") or "UNKNOWN"
        fmt_counts[fmt] += 1

        cta = a.get("cta")
        if cta:
            cta_counts[cta] += 1

        plat = a.get("plat") or ""
        if plat:
            plat_combo_counts[plat] += 1
            for code in plat.split(","):
                code = code.strip()
                if code:
                    plat_single_counts[code] += 1

        st = a.get("st")
        if st:
            cadence[st] += 1

        slug = a.get("slug") or "(no product)"
        p = products[slug]
        p["n"] += 1
        p[fmt if fmt in ("VIDEO", "DCO", "CAROUSEL", "IMAGE") else "OTHER"] += 1
        if st:
            if p["first"] is None or st < p["first"]:
                p["first"] = st
            if p["last"] is None or st > p["last"]:
                p["last"] = st

        blob = " ".join(filter(None, [a.get("ttl"), a.get("cap"), a.get("bd")]))
        scripts = detect_scripts(blob)
        for s in scripts:
            lang_hits[s] += 1
            if len(lang_examples[s]) < 3:
                lang_examples[s].append(a.get("id"))

        if "{{" in (a.get("ttl") or "") or "{{" in (a.get("bd") or ""):
            templated.append(a.get("id"))

        hook = (a.get("ttl") or "").strip()
        if hook:
            hook_to_slugs[hook].add(slug)

    repeated_hooks = {
        hook: sorted(slugs)
        for hook, slugs in hook_to_slugs.items()
        if len(slugs) > 1
    }

    product_breakdown = []
    for slug, p in sorted(products.items(), key=lambda kv: -kv[1]["n"]):
        product_breakdown.append({
            "slug": slug,
            "count": p["n"],
            "video": p["VIDEO"],
            "dco": p["DCO"],
            "carousel": p["CAROUSEL"],
            "image": p["IMAGE"],
            "other": p["OTHER"],
            "first_live": p["first"],
            "last_live": p["last"],
        })

    non_latin_total = sum(1 for a in ads if detect_scripts(
        " ".join(filter(None, [a.get("ttl"), a.get("cap"), a.get("bd")]))))

    return {
        "total_unique_ads": total,
        "format_counts": dict(fmt_counts.most_common()),
        "cta_counts": dict(cta_counts.most_common()),
        "platform_single_counts": dict(plat_single_counts.most_common()),
        "platform_combo_counts": dict(plat_combo_counts.most_common()),
        "cadence_by_date": dict(sorted(cadence.items())),
        "product_breakdown": product_breakdown,
        "language": {
            "non_latin_script_ad_count": non_latin_total,
            "non_latin_script_pct": round(100 * non_latin_total / total, 1) if total else 0,
            "scripts_found": {
                name: {"count": lang_hits[name], "example_ids": lang_examples[name]}
                for name in lang_hits
            },
            "note": ("Script detection catches native-script regional language. It will NOT "
                     "catch romanised/transliterated regional-language copy (e.g. Hindi "
                     "written in Latin letters) — skim a sample of ads before claiming "
                     "'zero regional-language creative' if the brand plausibly does this."),
        },
        "templated_placeholder_ad_ids": templated,
        "templated_placeholder_count": len(templated),
        "repeated_hooks_across_products": repeated_hooks,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", help="Path to the cleaned ads JSON array")
    ap.add_argument("--out", help="Also write the summary JSON to this path")
    ap.add_argument("--pretty", action="store_true", help="Pretty-print stdout")
    args = ap.parse_args()

    ads = load(args.input)
    summary = analyze(ads)

    indent = 2 if args.pretty else None
    out_str = json.dumps(summary, indent=indent, ensure_ascii=False)
    print(out_str)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(json.dumps(summary, indent=2, ensure_ascii=False))
        print(f"\nWrote summary to {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
