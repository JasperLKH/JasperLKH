import math
import pathlib
import random

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets"

W, H = 1000, 280
CYCLE = 24.0                                                     
\
KT = "0;0.40;0.50;0.90;1"
A_VALS = "1;1;0;0;1"           
B_VALS = "0;0;1;1;0"         

def fade(vals):
    return (f'<animate attributeName="opacity" values="{vals}" keyTimes="{KT}" '
            f'dur="{CYCLE}s" repeatCount="indefinite" calcMode="spline" '
            f'keySplines=".4 0 .6 1;.4 0 .6 1;.4 0 .6 1;.4 0 .6 1"/>')

def petal(rng):
    x = rng.uniform(20, W - 20)
    dur = rng.uniform(7, 14)
    delay = -rng.uniform(0, 14)
    s = rng.uniform(0.55, 1.25)
    sway = rng.uniform(30, 90)
    rot = rng.choice([360, -360])
    op = rng.uniform(0.45, 0.9)
    hue = rng.choice(["#ffffff", "#ffd9ea", "#f4f7fc", "#ffc2e0"])
    return f'''    <g transform="translate({x:.0f},-40)">
      <animateTransform attributeName="transform" type="translate" additive="sum"
        values="0,-40; 0,{H+40}" dur="{dur:.1f}s" begin="{delay:.1f}s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="translate" additive="sum"
        values="0,0; {sway:.0f},0; -{sway*0.6:.0f},0; 0,0" dur="{dur*0.55:.1f}s" begin="{delay:.1f}s"
        repeatCount="indefinite" calcMode="spline" keySplines=".4 0 .6 1;.4 0 .6 1;.4 0 .6 1" keyTimes="0;.33;.66;1"/>
      <g transform="scale({s:.2f})" opacity="{op:.2f}">
        <path d="M0,0 C5,-7 13,-7 15,0 C13,7 5,7 0,0 Z" fill="{hue}"/>
        <animateTransform attributeName="transform" type="rotate" additive="sum"
          values="0;{rot}" dur="{dur*0.4:.1f}s" begin="{delay:.1f}s" repeatCount="indefinite"/>
      </g>
    </g>'''

def flake(rng):
    pass
    x = rng.uniform(10, W - 10)
    dur = rng.uniform(11, 20)
    delay = -rng.uniform(0, 20)
    sway = rng.uniform(18, 55)
    op = rng.uniform(0.4, 0.95)
    crystal = rng.random() < 0.25
    if crystal:
        s = rng.uniform(0.5, 0.95)
        arms = "".join(
            f'<line x1="0" y1="0" x2="{7*math.cos(math.radians(a)):.1f}" y2="{7*math.sin(math.radians(a)):.1f}"/>'
            for a in range(0, 180, 30))
        shape = (f'<g stroke="#ffffff" stroke-width="1.4" stroke-linecap="round" '
                 f'transform="scale({s:.2f})">{arms}'
                 f'<animateTransform attributeName="transform" type="rotate" additive="sum" '
                 f'values="0;360" dur="{dur*0.55:.1f}s" begin="{delay:.1f}s" repeatCount="indefinite"/></g>')
    else:
        r = rng.uniform(1.2, 3.2)
        shape = f'<circle r="{r:.1f}" fill="#ffffff"/>'
    return f'''    <g transform="translate({x:.0f},-30)" opacity="{op:.2f}">
      <animateTransform attributeName="transform" type="translate" additive="sum"
        values="0,-30; 0,{H+30}" dur="{dur:.1f}s" begin="{delay:.1f}s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="translate" additive="sum"
        values="0,0; {sway:.0f},0; -{sway*0.7:.0f},0; 0,0" dur="{dur*0.5:.1f}s" begin="{delay:.1f}s"
        repeatCount="indefinite" calcMode="spline" keySplines=".4 0 .6 1;.4 0 .6 1;.4 0 .6 1" keyTimes="0;.33;.66;1"/>
      {shape}
    </g>'''

def star(rng):
    x, y = rng.uniform(10, W - 10), rng.uniform(8, 150)
    r, dur, delay = rng.uniform(0.7, 1.8), rng.uniform(1.6, 4.5), -rng.uniform(0, 4)
    return (f'    <circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="#ffffff">'
            f'<animate attributeName="opacity" values="0.15;1;0.15" dur="{dur:.1f}s" '
            f'begin="{delay:.1f}s" repeatCount="indefinite"/></circle>')

def ridge(y, amp, seed, fill, op, cap=None):
    pass
    r = random.Random(seed)
    pts, x = [], 0
    while x <= W:
        pts.append((x, y - abs(math.sin(x / r.uniform(90, 160)) * amp) - r.uniform(0, amp * .3)))
        x += 40
    crest = " ".join(f"L{px:.0f},{py:.0f}" for px, py in pts)
    out = f'    <path d="M-10,{H} {crest} L{W+10},{H} Z" fill="{fill}" opacity="{op}"/>'
    if cap:
        \
        open_crest = "M" + crest[1:]
        out += (f'\n    <path d="{open_crest}" fill="none" stroke="{cap}" stroke-width="3" '
                f'stroke-linejoin="round" stroke-linecap="round" stroke-opacity=".6"/>')
    return out

def torii(snow=False):
    caps = ""
    if snow:
        caps = ('<rect x="-26" y="2" width="146" height="5" rx="2" fill="#ffffff" opacity=".9"/>'
                '<rect x="-18" y="27" width="130" height="4" rx="2" fill="#ffffff" opacity=".75"/>')
    return f'''    <g transform="translate(120,132) scale(0.9)">
      <g fill="{'#141922' if snow else '#080b10'}" opacity=".92">
        <rect x="-6" y="18" width="14" height="120" rx="3"/>
        <rect x="86" y="18" width="14" height="120" rx="3"/>
        <rect x="-26" y="6" width="146" height="12" rx="4"/>
        <rect x="-18" y="30" width="130" height="9" rx="3"/>
        <rect x="42" y="10" width="10" height="26"/>
      </g>{caps}
    </g>'''

rng = random.Random(7)
petals = "\n".join(petal(rng) for _ in range(22))
stars = "\n".join(star(rng) for _ in range(60))
rng_s = random.Random(21)
flakes = "\n".join(flake(rng_s) for _ in range(34))

sakura_scene = f'''  <g>
    {fade(A_VALS)}
    <rect width="{W}" height="{H}" fill="url(#skyWarm)"/>
{stars}
    <circle cx="820" cy="82" r="90" fill="url(#haloWarm)">
      <animate attributeName="r" values="86;104;86" dur="7s" repeatCount="indefinite"/>
    </circle>
    <circle cx="820" cy="82" r="40" fill="url(#moonWarm)"/>
    <circle cx="800" cy="70" r="7" fill="#d7dee8" opacity=".5"/>
    <circle cx="836" cy="96" r="5" fill="#d7dee8" opacity=".4"/>
{ridge(255, 70, 3, '#151a23', 0.85)}
{ridge(272, 45, 11, '#0b0e14', 0.95)}
{torii(snow=False)}
{petals}
  </g>'''

snow_scene = f'''  <g>
    {fade(B_VALS)}
    <rect width="{W}" height="{H}" fill="url(#skyCold)"/>
{stars}
    <circle cx="820" cy="82" r="90" fill="url(#haloCold)">
      <animate attributeName="r" values="86;104;86" dur="7s" repeatCount="indefinite"/>
    </circle>
    <circle cx="820" cy="82" r="40" fill="url(#moonCold)"/>
    <circle cx="800" cy="70" r="7" fill="#e3e9f2" opacity=".4"/>
    <circle cx="836" cy="96" r="5" fill="#e3e9f2" opacity=".32"/>
{ridge(255, 70, 3, '#39424f', 0.92, cap='#ffffff')}
{ridge(272, 45, 11, '#171c25', 0.97, cap='#e6ecf5')}
{torii(snow=True)}
{flakes}
  </g>'''

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Jasper banner">
  <defs>
    <linearGradient id="skyWarm" x1="0" y1="0" x2="0.3" y2="1">
      <stop offset="0%" stop-color="#05070a"/><stop offset="45%" stop-color="#141922"/>
      <stop offset="75%" stop-color="#3d4757"/><stop offset="100%" stop-color="#aab6c8"/>
    </linearGradient>
    <linearGradient id="skyCold" x1="0" y1="0" x2="0.3" y2="1">
      <stop offset="0%" stop-color="#0c1016"/><stop offset="45%" stop-color="#2b333f"/>
      <stop offset="78%" stop-color="#8d99a9"/><stop offset="100%" stop-color="#ffffff"/>
    </linearGradient>
    <radialGradient id="moonWarm"><stop offset="0%" stop-color="#ffffff"/><stop offset="70%" stop-color="#eef2f8"/><stop offset="100%" stop-color="#cdd6e2"/></radialGradient>
    <radialGradient id="moonCold"><stop offset="0%" stop-color="#ffffff"/><stop offset="70%" stop-color="#f6f9ff"/><stop offset="100%" stop-color="#dee5ef"/></radialGradient>
    <radialGradient id="haloWarm"><stop offset="0%" stop-color="#eef2f8" stop-opacity=".5"/><stop offset="100%" stop-color="#eef2f8" stop-opacity="0"/></radialGradient>
    <radialGradient id="haloCold"><stop offset="0%" stop-color="#ffffff" stop-opacity=".5"/><stop offset="100%" stop-color="#ffffff" stop-opacity="0"/></radialGradient>

    <linearGradient id="neon" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#9aa5b6"/>
      <stop offset="50%" stop-color="#ffffff">
        <animate attributeName="stop-color" values="#ffffff;#ffffff;#ffffff;#ffffff;#ffffff"
          keyTimes="{KT}" dur="{CYCLE}s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#ff9ecb">
        <animate attributeName="stop-color" values="#ff9ecb;#ff9ecb;#ffd9ea;#ffd9ea;#ff9ecb"
          keyTimes="{KT}" dur="{CYCLE}s" repeatCount="indefinite"/>
      </stop>
      <animate attributeName="x1" values="-1;0;-1" dur="6s" repeatCount="indefinite"/>
      <animate attributeName="x2" values="0;2;0" dur="6s" repeatCount="indefinite"/>
    </linearGradient>

    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="6" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="softglow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="2.2" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="frame"><rect width="{W}" height="{H}" rx="18"/></clipPath>
  </defs>

  <g clip-path="url(#frame)">
{sakura_scene}
{snow_scene}

    <rect x="0" y="228" width="{W}" height="2" fill="url(#neon)" opacity=".85" filter="url(#softglow)"/>
    <rect x="0" y="140" width="{W}" height="90" fill="#050a18" opacity=".18"/>

    <g filter="url(#glow)">
      <text x="500" y="146" text-anchor="middle"
        font-family="'Segoe UI','Helvetica Neue',Arial,sans-serif" font-size="66" font-weight="800"
        letter-spacing="10" fill="url(#neon)">JASPER</text>
    </g>
    <text x="500" y="180" text-anchor="middle"
      font-family="'Fira Code','JetBrains Mono',ui-monospace,monospace" font-size="15"
      fill="#dbe3ee" letter-spacing="4" opacity=".92">&lt; keep grinding /&gt;</text>
    <text x="500" y="206" text-anchor="middle"
      font-family="'Segoe UI',Arial,sans-serif" font-size="12" fill="#9aa5b6" letter-spacing="8" opacity=".82">S O F T W A R E &#160;&#160; E N G I N E E R</text>

    <rect x="-260" y="0" width="260" height="{H}" fill="#ffffff" opacity=".05">
      <animate attributeName="x" values="-260;{W}" dur="9s" repeatCount="indefinite"/>
    </rect>
    <rect width="{W}" height="{H}" rx="18" fill="none" stroke="#ff9ecb" stroke-opacity=".4" stroke-width="2"/>
  </g>
</svg>
'''

(OUT / "hero.svg").write_text(svg)
print("bytes:", len(svg))
