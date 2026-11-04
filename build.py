"""Builds a single self-contained index.html from index.src.html.
Edit index.src.html, then run:  python3 build.py
Every src="assets/..." image gets inlined as a data URI."""
import base64, re, pathlib
root = pathlib.Path(__file__).parent
html = (root / "index.src.html").read_text(encoding="utf-8")
MIME = {".png": "image/png", ".svg": "image/svg+xml", ".webp": "image/webp"}
def inline(m):
    p = root / m.group(2)
    mime = MIME.get(p.suffix, "image/jpeg")
    return f'{m.group(1)}="data:{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"'
out = re.sub(r'(src|href)="(assets/[^"]+\.(?:png|jpg|svg|webp))"', inline, html)
(root / "index.html").write_text(out, encoding="utf-8")
print(f"index.html written ({len(out)/1e6:.1f} MB)")
