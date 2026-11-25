"""Animated, theme-aware SVGs for the profile README, in mdxcn's visual language:
dashed frame, '+' corners, [ TITLE ] on the top edge, mono type, one accent.
Each figure is written as <name>-dark.svg and <name>-light.svg.
Animations use CSS keyframes + SMIL only (GitHub serves README SVGs as images: no JS, no external fonts)."""
import html, json, os, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
os.makedirs(OUT, exist_ok=True)

THEMES = {
    "dark": dict(fg="#e6edf3", muted="#8b949e", faint="#30363d", frame="#484f58", accent="#2fc5f0", accent2="#f0b429", ok="#3fb950", bad="#f85149", track="#21262d"),
    "light": dict(fg="#1f2328", muted="#59636e", faint="#d1d9e0", frame="#afb8c1", accent="#0a73b0", accent2="#b7791f", ok="#1a7f37", bad="#cf222e", track="#eaeef2"),
}
FONT = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"
CW = 0.602  # mono advance, em


def esc(s):
    return html.escape(s, quote=True)


def base_css(t):
    return f"""
  text {{ font-family: {FONT}; fill: {t['fg']}; }}
  .m {{ fill: {t['muted']}; }} .a {{ fill: {t['accent']}; }} .a2 {{ fill: {t['accent2']}; }}
  .ok {{ fill: {t['ok']}; }} .bad {{ fill: {t['bad']}; }}
  .fr {{ stroke: {t['frame']}; stroke-width: 1; stroke-dasharray: 2 4; fill: none; }}
  .cn {{ fill: {t['frame']}; }}
  .in {{ opacity: 0; animation: in .5s ease-out forwards; }}
  @keyframes in {{ from {{ opacity: 0; transform: translateY(4px); }} to {{ opacity: 1; transform: none; }} }}
  @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; opacity: 1 !important; }} }}
"""


def frame(w, h, title, t, size=14):
    """Dashed box with + corners and a [ TITLE ] gap on the top edge."""
    cap = f"[ {title.upper()} ]"
    capw = len(cap) * size * CW
    x0, y0, x1, y1 = 8, 12, w - 8, h - 8
    cx = w / 2
    gap = capw / 2 + 12
    parts = [
        f'<path class="fr" d="M{cx-gap} {y0} H{x0} V{y1} H{x1} V{y0} H{cx+gap}"/>',
    ]
    for (x, y) in [(x0, y0), (x1, y0), (x0, y1), (x1, y1)]:
        parts.append(f'<text x="{x}" y="{y+4.5}" text-anchor="middle" font-size="13" class="cn" style="fill:{t["frame"]}">+</text>')
    parts.append(f'<text x="{cx}" y="{y0+5}" text-anchor="middle" font-size="{size}" class="a" letter-spacing=".5">{esc(cap)}</text>')
    return "\n".join(parts)


def svg(w, h, body, css, t, label):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(label)}">
<title>{esc(label)}</title>
<style>{base_css(t)}{css}</style>
{body}
</svg>
"""


def typed(x, y, s, start, dur, cls="", size=15, cid="c", weight="400"):
    """Text revealed char by char with a stepped clip (SMIL, frozen at the end)."""
    w = len(s) * size * CW + 4
    n = max(1, len(s))
    return f"""<clipPath id="{cid}"><rect x="{x-1}" y="{y-size}" height="{size*1.5}" width="0">
  <animate attributeName="width" from="0" to="{w:.1f}" begin="{start}s" dur="{dur}s" fill="freeze" calcMode="discrete"
   values="{';'.join(f'{w*i/n:.1f}' for i in range(n+1))}"/></rect></clipPath>
<text x="{x}" y="{y}" font-size="{size}" class="{cls}" font-weight="{weight}" clip-path="url(#{cid})" xml:space="preserve">{esc(s)}</text>"""


# ---------------------------------------------------------------- header
def header(t):
    W, H = 860, 250
    lines = [
        ("$ ", "whoami", "", 0.3),
        ("", "suryansh pratap singh", "big", 1.0),
        ("", "cs @ manipal university jaipur · class of 2027", "m", 2.0),
        ("$ ", "cat focus.txt", "", 3.2),
        ("", "full-stack + ai products, shipped to real users.", "a", 4.0),
    ]
    body = [frame(W, H, "hello", t)]
    y = 58
    for i, (prompt, s, cls, start) in enumerate(lines):
        size = 26 if cls == "big" else 15
        x = 44
        if prompt:
            body.append(f'<text x="{x}" y="{y}" font-size="15" class="a in" style="animation-delay:{start}s">$</text>')
            x += 2 * 15 * CW
        dur = max(0.3, len(s) * 0.035)
        body.append(typed(x, y, s, start, dur, "" if cls == "big" else cls, size, f"h{i}", "700" if cls == "big" else "400"))
        last_y = y
        y += 44 if cls == "big" else (30 if i in (0, 3) else 38)
        if cls == "big":
            y -= 4
    # blinking cursor after last line
    last = lines[-1][1]
    cx = 44 + len(last) * 15 * CW + 6
    body.append(f'<rect x="{cx:.1f}" y="{last_y-14}" width="9" height="18" fill="{t["accent"]}" class="cur"/>')
    # right side: live status
    body.append(f'''<g class="in" style="animation-delay:4.8s">
  <circle cx="{W-220}" cy="{H-44}" r="4.5" fill="{t['ok']}"><animate attributeName="r" values="4.5;6.5;4.5" dur="2.4s" repeatCount="indefinite"/>
  <animate attributeName="opacity" values="1;.55;1" dur="2.4s" repeatCount="indefinite"/></circle>
  <text x="{W-206}" y="{H-39}" font-size="13" class="m">open to sde roles</text></g>''')
    css = """.cur { opacity: 0; animation: blink 1s steps(1) 4.9s infinite; }
@keyframes blink { 0% { opacity: 1; } 50% { opacity: 0; } }"""
    return svg(W, H, "\n".join(body), css, t, "Suryansh Pratap Singh. CS at Manipal University Jaipur, class of 2027. Full-stack and AI products, shipped to real users.")


# ---------------------------------------------------------------- stat strip (GraphStat style)
def stats(t):
    W, H = 860, 150
    items = [("68,000+", "teams at sih 2025. we won"), ("1st", "codeclash 2.0, 1,000+ teams"), ("2nd", "iic 2.0 national hackathon")]
    body = [frame(W, H, "so far", t)]
    colw = (W - 80) / 3
    for i, (v, l) in enumerate(items):
        x = 44 + i * colw
        d = 0.2 + i * 0.25
        cls = "a" if i == 0 else ""
        body.append(f'<g class="in" style="animation-delay:{d}s"><text x="{x}" y="78" font-size="36" font-weight="600" class="{cls}">{esc(v)}</text>')
        body.append(f'<text x="{x}" y="110" font-size="13.5" class="m">{esc(l)}</text></g>')
        lw = len(v) * 36 * CW
        body.append(f'<rect x="{x}" y="88" height="2" width="0" fill="{t["accent"] if i==0 else t["faint"]}"><animate attributeName="width" from="0" to="{lw:.0f}" begin="{d+0.3}s" dur=".6s" fill="freeze"/></rect>')
    return svg(W, H, "\n".join(body), "", t, "Won SIH 2025 among 68,000+ teams. 1st at CodeClash 2.0 among 1,000+ teams. Runner-up at the IIC 2.0 national hackathon.")


# ---------------------------------------------------------------- project cards
def card(t, key):
    W, H = 420, 210
    P = {
        "wavewatch": ("wavewatch", "coastal hazard reporting for", "analysts and citizens", "react · express · mongodb · twilio", "won sih 2025"),
        "internsetu": ("internsetu", "resume in, internships ranked", "by fit, then a mock interview", "react · fastapi · chroma · gemini", "runner-up iic 2.0"),
        "sunskip": ("sunskip", "routes ranked by minutes", "spent in direct sun", "react · fastapi · postgis · aws", "aws sustainability hack"),
        "gradex": ("gradex", "exams graded against a model", "answer, with feedback", "fastapi · postgresql · bert · claude", "side project"),
    }[key]
    title, l1, l2, stack, result = P
    body = [frame(W, H, title, t, 13)]
    body.append(f'<text x="30" y="52" font-size="14">{esc(l1)}</text>')
    body.append(f'<text x="30" y="72" font-size="14">{esc(l2)}</text>')
    body.append(f'<text x="30" y="{H-56}" font-size="12" class="m">{esc(stack)}</text>')
    body.append(f'<text x="30" y="{H-30}" font-size="12.5" class="a">● {esc(result)}</text>')
    body.append(f'<text x="{W-30}" y="{H-30}" font-size="12.5" class="m" text-anchor="end">open ↗</text>')
    ax, ay, aw, ah = 30, 90, W - 60, 50  # animation area
    a = t["accent"]
    css = ""
    if key == "wavewatch":
        # two scrolling sine waves + a pulsing alert pin
        import math
        def wave(amp, per, ph):
            pts = []
            for i in range(0, int(aw * 2) + 1, 4):
                pts.append(f"{ax + i:.1f},{ay + ah/2 + amp*math.sin((i/per)*2*math.pi + ph):.1f}")
            return "M" + " L".join(pts)
        body.append(f'<clipPath id="wc"><rect x="{ax}" y="{ay}" width="{aw}" height="{ah}"/></clipPath><g clip-path="url(#wc)">')
        body.append(f'<path d="{wave(9, 90, 0)}" fill="none" stroke="{a}" stroke-width="2"><animateTransform attributeName="transform" type="translate" from="0 0" to="-90 0" dur="2.2s" repeatCount="indefinite"/></path>')
        body.append(f'<path d="{wave(6, 60, 1)}" fill="none" stroke="{t["muted"]}" stroke-width="1.2" opacity=".6"><animateTransform attributeName="transform" type="translate" from="-60 0" to="0 0" dur="3s" repeatCount="indefinite"/></path></g>')
        px = ax + aw - 40
        body.append(f'<circle cx="{px}" cy="{ay+10}" r="5" fill="{t["bad"]}"/><circle cx="{px}" cy="{ay+10}" r="5" fill="none" stroke="{t["bad"]}"><animate attributeName="r" values="5;16" dur="1.6s" repeatCount="indefinite"/><animate attributeName="opacity" values="1;0" dur="1.6s" repeatCount="indefinite"/></circle>')
    elif key == "internsetu":
        rows = [("backend intern", .92), ("ml intern", .74), ("design intern", .41)]
        for i, (n, f) in enumerate(rows):
            y = ay + 4 + i * 17
            body.append(f'<text x="{ax}" y="{y+9}" font-size="11.5" class="m">{n}</text>')
            bx = ax + 130; bw = aw - 130
            body.append(f'<rect x="{bx}" y="{y}" width="{bw}" height="9" fill="{t["track"]}"/>')
            col = a if i == 0 else t["muted"]
            body.append(f'<rect x="{bx}" y="{y}" width="0" height="9" fill="{col}"><animate attributeName="width" values="0;{bw*f:.0f};{bw*f:.0f};0" keyTimes="0;.25;.85;1" dur="5s" begin="{i*0.2}s" repeatCount="indefinite"/></rect>')
    elif key == "sunskip":
        # sun travelling an arc; path segments turn shaded/sunny
        cx0, cy0, r = ax + aw / 2, ay + ah - 6, aw / 2 - 10
        body.append(f'<path id="arc" d="M{cx0-r} {cy0} A{r} {ah-14} 0 0 1 {cx0+r} {cy0}" fill="none" stroke="{t["faint"]}" stroke-dasharray="2 4"/>')
        body.append(f'<circle r="7" fill="{t["accent2"]}"><animateMotion dur="6s" repeatCount="indefinite" rotate="0"><mpath href="#arc"/></animateMotion></circle>')
        segs = 12
        for i in range(segs):
            x = ax + i * aw / segs
            shade = i % 4 in (1, 2)
            col = t["ok"] if shade else t["accent2"]
            body.append(f'<rect x="{x+1:.1f}" y="{ay+ah-2}" width="{aw/segs-3:.1f}" height="4" fill="{col}" opacity=".85"/>')
    elif key == "gradex":
        marks = [("q1", "✓", "ok", "8/10"), ("q2", "✓", "ok", "9/10"), ("q3", "✗", "bad", "3/10")]
        for i, (q, m, c, s) in enumerate(marks):
            y = ay + 12 + i * 17
            d = 0.5 + i * 0.6
            body.append(f'<g class="pop" style="animation-delay:{d}s"><text x="{ax}" y="{y}" font-size="12" class="m">{q}</text>'
                        f'<text x="{ax+40}" y="{y}" font-size="13" class="{c}">{m}</text>'
                        f'<text x="{ax+64}" y="{y}" font-size="12">{s}</text></g>')
        css = """.pop { opacity: 0; animation: pop 6s infinite; }
@keyframes pop { 0%, 8% { opacity: 0; } 14%, 88% { opacity: 1; } 100% { opacity: 0; } }"""
    return svg(W, H, "\n".join(body), css, t, f"{title}: {l1} {l2}. {stack}. {result}.")


# ---------------------------------------------------------------- timeline (GraphTimeline style)
def timeline(t):
    ev = [
        ("2025", "won smart india hackathon", "wavewatch, built the full stack solo", "done"),
        ("apr 2026", "backend intern @ billcut", "node.js / express backend for billgpt", "done"),
        ("jun 2026", "sde intern @ better", "integrations + auth for operate, an incident rca agent", "done"),
        ("now", "building lerno", "ai maths lessons, live at math.lerno.dev", "now"),
        ("2027", "graduating", "open to sde roles", "next"),
    ]
    W = 860
    H = 70 + len(ev) * 56
    body = [frame(W, H, "journey", t)]
    x0, y = 50, 56
    for i, (d, l, n, st) in enumerate(ev):
        delay = 0.3 + i * 0.45
        if i < len(ev) - 1:
            body.append(f'<line x1="{x0}" y1="{y+8}" x2="{x0}" y2="{y+48}" stroke="{t["faint"]}" stroke-width="1.5" stroke-dasharray="40" stroke-dashoffset="40"><animate attributeName="stroke-dashoffset" from="40" to="0" begin="{delay+.3}s" dur=".4s" fill="freeze"/></line>')
        if st == "next":
            dot = f'<circle cx="{x0}" cy="{y}" r="5" fill="none" stroke="{t["muted"]}" stroke-width="1.5"/>'
        elif st == "now":
            dot = (f'<circle cx="{x0}" cy="{y}" r="5.5" fill="{t["accent"]}"/><circle cx="{x0}" cy="{y}" r="5.5" fill="none" stroke="{t["accent"]}">'
                   f'<animate attributeName="r" values="5.5;13" dur="1.8s" repeatCount="indefinite"/><animate attributeName="opacity" values=".9;0" dur="1.8s" repeatCount="indefinite"/></circle>')
        else:
            dot = f'<circle cx="{x0}" cy="{y}" r="5" fill="{t["fg"]}"/>'
        lc = "a" if st == "now" else ("m" if st == "next" else "")
        body.append(f'<g class="in" style="animation-delay:{delay}s">{dot}'
                    f'<text x="{x0+24}" y="{y+5}" font-size="14" class="m">{esc(d)}</text>'
                    f'<text x="{x0+140}" y="{y+5}" font-size="15" class="{lc}">{esc(l)}</text>'
                    f'<text x="{x0+140}" y="{y+26}" font-size="13" class="m">{esc(n)}</text></g>')
        y += 56
    return svg(W, H, "\n".join(body), "", t, "Journey: won SIH 2025; backend intern at BillCut Apr 2026; SDE intern at Better Jun 2026; building Lerno now; graduating 2027.")


# ---------------------------------------------------------------- stack (GraphSpec style)
def stack(t):
    rows = [
        ("languages", "typescript · python · java · c++"),
        ("frontend", "react · next.js · tailwind"),
        ("backend", "fastapi · node.js · express"),
        ("data", "postgresql · mongodb · supabase · firebase"),
        ("ai", "claude api · manim · rag (faiss, pinecone)"),
        ("infra", "docker · aws · vercel · modal"),
        ("mobile", "flutter · swiftui"),
    ]
    W = 860
    H = 60 + len(rows) * 28
    body = [frame(W, H, "stack", t)]
    y = 54
    for i, (k, v) in enumerate(rows):
        body.append(f'<g class="in" style="animation-delay:{0.15+i*0.12}s"><text x="44" y="{y}" font-size="14" class="m">{k}</text><text x="190" y="{y}" font-size="14" class="{"a" if k=="ai" else ""}">{esc(v)}</text></g>')
        y += 28
    return svg(W, H, "\n".join(body), "", t, "Stack: " + "; ".join(f"{k}: {v}" for k, v in rows))



# ---------------------------------------------------------------- vote (GraphRank style), data from votes.json
def votes_fig(t, data):
    items = sorted(data["topics"].items(), key=lambda kv: (-kv[1], kv[0]))
    total = sum(v for _, v in items)
    top = max([v for _, v in items] + [1])
    W = 860
    H = 96 + len(items) * 34
    body = [frame(W, H, "next lesson", t)]
    y = 58
    bx, bw = 290, 430
    for i, (name, v) in enumerate(items):
        lead = i == 0 and v > 0 and (len(items) < 2 or v > items[1][1])
        frac = v / top if top else 0
        d = 0.2 + i * 0.12
        body.append(f'<text x="44" y="{y+11}" font-size="14" class="{"a" if lead else ""}">{esc(name)}</text>')
        body.append(f'<rect x="{bx}" y="{y}" width="{bw}" height="14" fill="{t["track"]}"/>')
        body.append(f'<rect x="{bx}" y="{y}" height="14" width="0" fill="{t["accent"] if lead else t["muted"]}">'
                    f'<animate attributeName="width" from="0" to="{bw*frac:.0f}" begin="{d}s" dur=".8s" fill="freeze" calcMode="spline" keySplines=".2 .8 .2 1"/></rect>')
        body.append(f'<text x="{W-44}" y="{y+11}" font-size="14" text-anchor="end" class="{"a" if lead else "m"}">{v}</text>')
        y += 34
    body.append(f'<text x="44" y="{H-30}" font-size="12.5" class="m">{total} vote{"s" if total != 1 else ""} · one per github account · updates itself</text>')
    return svg(W, H, "\n".join(body), "", t, "Votes for the next Lerno lesson: " + ", ".join(f"{k} {v}" for k, v in items))

FIGS = {"header": header, "stats": stats, "timeline": timeline, "stack": stack}
for name, fn in FIGS.items():
    for th, t in THEMES.items():
        open(f"{OUT}/{name}-{th}.svg", "w").write(fn(t))
for key in ["wavewatch", "internsetu", "sunskip", "gradex"]:
    for th, t in THEMES.items():
        open(f"{OUT}/card-{key}-{th}.svg", "w").write(card(t, key))
here = os.path.dirname(os.path.abspath(__file__))
vpath = os.path.join(here, "..", "votes.json")
if os.path.exists(vpath):
    data = json.load(open(vpath))
    for th, t in THEMES.items():
        open(f"{OUT}/votes-{th}.svg", "w").write(votes_fig(t, data))
print(sorted(os.listdir(OUT)))
