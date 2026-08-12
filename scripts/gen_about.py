
import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"

W, H = 1000, 306
PAD = 34
LEFT_W = 742                                                         
AV_CX, AV_CY, AV_R = 862, 170, 76

\
SNOW, SILVER, STEEL = "#ffffff", "#dbe3ee", "#9aa5b6"
PINK = "#ff9ecb"                                                             
TEXT, DIM = "#eef2f8", "#8d97a8"
MONO = "'Fira Code','JetBrains Mono',ui-monospace,SFMono-Regular,monospace"
SANS = "'Segoe UI','Helvetica Neue',Arial,sans-serif"

SKILLS = ["Java", "Spring Boot", "Python", "TypeScript", "PostgreSQL", "Docker", "AWS"]

def label(x, y, s, color=SILVER):
    return (f'    <text x="{x}" y="{y}" font-family="{MONO}" font-size="10.5" letter-spacing="2.6" '
            f'fill="{color}" opacity=".8">{s}</text>')

def body(x, y, s, size=15, color=TEXT, weight="400", family=SANS):
    return (f'    <text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'fill="{color}">{s}</text>')

def chips(x, y, items, maxw, lh=34):
    pass
    out, cx, cy = [], x, y
    for i, s in enumerate(items):
        w = len(s) * 7.6 + 24
        if cx + w > x + maxw:
            cx, cy = x, cy + lh
        hue = [SNOW, SILVER, PINK][i % 3]
        out.append(
            f'    <g>'
            f'<rect x="{cx:.0f}" y="{cy}" width="{w:.0f}" height="26" rx="13" fill="{hue}" fill-opacity=".08" '
            f'stroke="{hue}" stroke-opacity=".5" stroke-width="1"/>'
            f'<text x="{cx + w/2:.0f}" y="{cy + 17.5}" text-anchor="middle" font-family="{MONO}" '
            f'font-size="12" fill="{hue}" fill-opacity=".95">{s}</text>'
            f'<animate attributeName="opacity" values=".55;1;1;.55" keyTimes="0;.15;.85;1" '
            f'dur="5s" begin="{i * 0.18:.2f}s" repeatCount="indefinite"/></g>')
        cx += w + 9
    return "\n".join(out)

def bullets(x, y, items, colw=250, lh=24):
    pass
    out = []
    for i, s in enumerate(items):
        bx = x + (i % 2) * colw
        by = y + (i // 2) * lh
        out.append(f'    <rect x="{bx}" y="{by - 8}" width="6" height="6" fill="{PINK}" '
                   f'transform="rotate(45 {bx + 3} {by - 5})"/>')
        out.append(f'    <text x="{bx + 16}" y="{by}" font-family="{SANS}" font-size="15" '
                   f'fill="{TEXT}">{s}</text>')
    return "\n".join(out)

def bracket(x, y, sx, sy):
    return (f'    <path d="M{x + 20*sx},{y} L{x},{y} L{x},{y + 20*sy}" fill="none" stroke="url(#edge)" '
            f'stroke-width="2" stroke-linecap="round" opacity=".9"/>')

def avatar():
    pass
    found = next((p for ext in ("png", "jpg", "jpeg", "webp")
                  for p in [OUT / f"avatar.{ext}"] if p.exists()), None)
    if found:
        raw = found.read_bytes()
        \
\
        if raw[:8] == b"\x89PNG\r\n\x1a\n":
            mime = "png"
        elif raw[:2] == b"\xff\xd8":
            mime = "jpeg"
        elif raw[:4] == b"RIFF" and raw[8:12] == b"WEBP":
            mime = "webp"
        else:
            raise SystemExit(f"{found}: unrecognised image format")
        b64 = base64.b64encode(raw).decode()
        inner = (f'<image href="data:image/{mime};base64,{b64}" '
                 f'x="{AV_CX - AV_R}" y="{AV_CY - AV_R}" width="{AV_R*2}" height="{AV_R*2}" '
                 f'preserveAspectRatio="xMidYMid slice" clip-path="url(#avclip)"/>')
    else:
        inner = (f'<circle cx="{AV_CX}" cy="{AV_CY}" r="{AV_R}" fill="url(#avph)"/>'
                 f'<text x="{AV_CX}" y="{AV_CY - 2}" text-anchor="middle" font-family="{MONO}" '
                 f'font-size="12" letter-spacing="2" fill="{SILVER}" opacity=".8">AVATAR</text>'
                 f'<text x="{AV_CX}" y="{AV_CY + 18}" text-anchor="middle" font-family="{MONO}" '
                 f'font-size="9" fill="{DIM}" opacity=".75">assets/avatar.png</text>')
    return f'''    <g>
      <circle cx="{AV_CX}" cy="{AV_CY}" r="{AV_R + 16}" fill="url(#avglow)"/>
      {inner}
      <circle cx="{AV_CX}" cy="{AV_CY}" r="{AV_R + 4}" fill="none" stroke="url(#edge)" stroke-width="2" opacity=".9"/>
      <circle cx="{AV_CX}" cy="{AV_CY}" r="{AV_R + 13}" fill="none" stroke="{PINK}" stroke-opacity=".55"
              stroke-width="1.2" stroke-dasharray="3 9" stroke-linecap="round">
        <animateTransform attributeName="transform" type="rotate" from="0 {AV_CX} {AV_CY}"
          to="360 {AV_CX} {AV_CY}" dur="26s" repeatCount="indefinite"/>
      </circle>
    </g>'''

def flakes():
    pass
    spec = [(120, 19, -3), (300, 24, -9), (470, 17, -14), (655, 27, -5), (735, 21, -18)]
    out = []
    for x, dur, delay in spec:
        out.append(f'''    <g transform="translate({x},-16)" opacity=".3">
      <animateTransform attributeName="transform" type="translate" additive="sum"
        values="0,-16; 0,{H+16}" dur="{dur}s" begin="{delay}s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="translate" additive="sum"
        values="0,0; 30,0; -20,0; 0,0" dur="{dur*0.6:.1f}s" begin="{delay}s" repeatCount="indefinite"
        calcMode="spline" keySplines=".4 0 .6 1;.4 0 .6 1;.4 0 .6 1" keyTimes="0;.33;.66;1"/>
      <circle r="2.4" fill="{SNOW}"/>
    </g>''')
    return "\n".join(out)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="About panel">
  <defs>
    <linearGradient id="panel" x1="0" y1="0" x2="0.6" y2="1">
      <stop offset="0%" stop-color="#161a21"/><stop offset="60%" stop-color="#0d0f14"/><stop offset="100%" stop-color="#181c24"/>
    </linearGradient>
    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{STEEL}"/><stop offset="50%" stop-color="{SNOW}"/><stop offset="100%" stop-color="{PINK}"/>
      <animate attributeName="x1" values="-1;0;-1" dur="7s" repeatCount="indefinite"/>
      <animate attributeName="x2" values="0;2;0" dur="7s" repeatCount="indefinite"/>
    </linearGradient>
    <radialGradient id="avglow">
      <stop offset="60%" stop-color="{SNOW}" stop-opacity=".18"/>
      <stop offset="100%" stop-color="{SNOW}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="avph">
      <stop offset="0%" stop-color="#262c36"/><stop offset="100%" stop-color="#12151b"/>
    </radialGradient>
    <filter id="soft" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="2" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="card"><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="16"/></clipPath>
    <clipPath id="avclip"><circle cx="{AV_CX}" cy="{AV_CY}" r="{AV_R}"/></clipPath>
  </defs>

  <g clip-path="url(#card)">
    <rect width="{W}" height="{H}" fill="url(#panel)"/>

    <g stroke="{SNOW}" stroke-opacity=".04" stroke-width="1">
      {"".join(f'<line x1="{i}" y1="0" x2="{i}" y2="{H}"/>' for i in range(0, W, 40))}
      {"".join(f'<line x1="0" y1="{j}" x2="{W}" y2="{j}"/>' for j in range(0, H, 40))}
    </g>

{flakes()}

{body(PAD, 52, "KA HO LEE", size=27, weight="800")}
{body(PAD + 152, 52, "&#183;", size=27, color=DIM)}
{body(PAD + 172, 52, "JASPER", size=27, weight="800", color=SILVER)}
{body(PAD, 76, "Software Engineer &#183; building agent systems", size=14, color=DIM)}

    <rect x="{PAD}" y="99" width="{LEFT_W - PAD}" height="2" fill="url(#edge)" opacity=".85" filter="url(#soft)"/>

{label(PAD, 128, "CURRENT QUEST")}
{bullets(PAD, 154, ["Multi-agent systems", "LLM", "Distributed systems", "SaaS"])}

{label(PAD, 214, "EQUIPPED")}
{chips(PAD, 224, SKILLS, maxw=LEFT_W - PAD - 30)}

{label(PAD, 280, "CURRENTLY", color=PINK)}
{body(PAD + 104, 280, "Looking for a graduate software engineering role", size=13, color=TEXT)}

    <g transform="translate({W - PAD - 116},18)">
      <rect width="116" height="26" rx="13" fill="{SNOW}" fill-opacity=".08" stroke="{SNOW}" stroke-opacity=".45"/>
      <circle cx="16" cy="13" r="3.5" fill="{PINK}">
        <animate attributeName="opacity" values="1;.25;1" dur="2.2s" repeatCount="indefinite"/>
      </circle>
      <text x="30" y="17.5" font-family="{MONO}" font-size="11" fill="{TEXT}" letter-spacing="1">HKU &#8217;27</text>
    </g>
{avatar()}

    <rect x="-300" y="0" width="300" height="{H}" fill="{SNOW}" opacity=".03">
      <animate attributeName="x" values="-300;{W}" dur="11s" repeatCount="indefinite"/>
    </rect>

{bracket(14, 14, 1, 1)}
{bracket(W - 14, 14, -1, 1)}
{bracket(14, H - 14, 1, -1)}
{bracket(W - 14, H - 14, -1, -1)}
  </g>
  <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="16" fill="none" stroke="url(#edge)" stroke-opacity=".45" stroke-width="2"/>
</svg>
'''

(OUT / "about.svg").write_text(svg)
print("bytes:", len(svg))
