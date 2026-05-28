#!/usr/bin/env python3
"""
generate-tokens.py
Đọc design-tokens.json → sinh ra css/base.css
Chạy: python3 scripts/generate-tokens.py
"""

import json
from pathlib import Path

root   = Path(__file__).parent.parent
tokens = json.loads((root / "design-tokens.json").read_text(encoding="utf-8"))

c  = tokens["colors"]
ty = tokens["typography"]
sp = tokens["spacing"]
r  = tokens["radius"]
sh = tokens["shadow"]

def var_line(prefix, key, token):
    name    = f"--{prefix}{key}"
    comment = f"   /* {token['note']} */" if token.get("note") else ""
    return f"  {name}: {token['value']};{comment}"

color_lines  = [var_line("color-", k, v) for k, v in c.items()]
typo_lines   = [var_line("", k, v)       for k, v in ty.items()]
space_lines  = [f"  --space-{k}: {v['value']};"  for k, v in sp.items()]
radius_lines = [f"  --radius-{k}: {v['value']};" for k, v in r.items()]
shadow_lines = [f"  --shadow-{k}: {v['value']};" for k, v in sh.items()]

css = f"""\
/* ================================================================
   css/base.css
   AUTO-GENERATED từ design-tokens.json — đừng edit file này trực tiếp.
   Thay đổi design-tokens.json rồi chạy: python3 scripts/generate-tokens.py
   ================================================================ */

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
img {{ display: block; max-width: 100%; }}
a {{ text-decoration: none; color: inherit; }}
ul {{ list-style: none; }}

:root {{
  /* ── Màu sắc — {tokens["meta"]["brand"]} ── */
{chr(10).join(color_lines)}

  /* ── Typography ── */
{chr(10).join(typo_lines)}

  /* ── Spacing ── */
{chr(10).join(space_lines)}

  /* ── Radius ── */
{chr(10).join(radius_lines)}

  /* ── Shadow ── */
{chr(10).join(shadow_lines)}

  --transition: {tokens["transition"]["value"]};
}}

html {{ font-size: 16px; scroll-behavior: smooth; }}
body {{
  font-family: var(--font-body);
  color: var(--color-text);
  background-color: var(--color-bg);
  line-height: 1.65;
}}
h1, h2, h3, h4 {{ font-family: var(--font-heading); line-height: 1.2; }}
h1 {{ font-size: clamp(2.4rem, 5vw, 4rem); }}
h2 {{ font-size: clamp(1.8rem, 3.5vw, 2.8rem); }}
h3 {{ font-size: 1.2rem; }}
p  {{ color: var(--color-text-muted); }}

.btn {{
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.75rem;
  border-radius: 100px;
  font-family: var(--font-body);
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  border: 2px solid transparent;
  transition: var(--transition);
  white-space: nowrap;
}}
.btn--primary   {{ background: var(--color-primary);   color: var(--color-white); }}
.btn--primary:hover {{ background: var(--color-dark); }}
.btn--secondary {{ background: var(--color-secondary); color: var(--color-white); }}
.btn--secondary:hover {{ background: var(--color-amber); }}
.btn--ghost {{
  background: transparent;
  color: var(--color-white);
  border-color: rgba(255,255,255,.5);
}}
.btn--ghost:hover {{ border-color: var(--color-white); background: rgba(255,255,255,.12); }}
.btn--outline {{
  background: transparent;
  color: var(--color-primary);
  border-color: var(--color-primary);
}}
.btn--outline:hover {{ background: var(--color-primary); color: var(--color-white); }}
.btn--lg   {{ padding: 1rem 2.25rem; font-size: 1rem; }}
.btn--full {{ width: 100%; justify-content: center; }}

.section__eyebrow {{
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--color-primary);
  margin-bottom: var(--space-xs);
}}
.section__header {{ text-align: center; margin-bottom: var(--space-lg); }}
.section__header h2 {{ margin-top: var(--space-xs); color: var(--color-text); }}
.section__header p  {{ max-width: 520px; margin: 0.75rem auto 0; }}
"""

out = root / "css" / "base.css"
out.write_text(css, encoding="utf-8")
print(f"✅  css/base.css generated từ design-tokens.json")
print(f"    Colors: {len(c)} | Spacing: {len(sp)} | Radius: {len(r)} | Shadow: {len(sh)}")
