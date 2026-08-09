from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
pat = re.compile(r"\s*<div class=\"announcement\">[\s\S]*?</div>\s*", re.M)
count = 0
for path in root.glob("*.html"):
    text = path.read_text(encoding="utf-8")
    new_text, n = pat.subn("\n", text, count=1)
    if n:
        path.write_text(new_text, encoding="utf-8")
        count += 1
        print("removed", path.name)
print("done", count)
