# Atlan Pulse — deployment

The Pulse landing page is live at `https://atlan-pulse.onrender.com`, deployed as a Render static site from a Blueprint (config lives in the repo, not the dashboard). Source: `github.com/mananaggrawal/atlan-pulse`, branch `master`. Auto-deploys on push to `master`.

The underlying web app (`atlas`, a Docker web service) and its Postgres database are separate, still-active services, deliberately left running alongside the static landing page — the landing page was added *in addition to* the app, not as a replacement.

**Note:** the absolute URLs in the landing page's HTML (Open Graph tags, canonical link) are hardcoded to `https://atlan-pulse.onrender.com`. If that service is ever renamed or moved to a custom domain, those tags need updating or link previews will break — Open Graph requires absolute URLs.

**Verified live (not assumed):** the root page and the OG preview image both return 200; the security headers declared in the Render blueprint are actually served; fonts load over TLS; no horizontal scroll at desktop or mobile widths.