import jinja2
from pathlib import Path
from collections import defaultdict

env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
template = env.get_template("template_pdf.md")

tds = defaultdict(set)
cours = {}

files = list(Path(".").rglob("*_*/**/*.pdf"))
files.sort()
for file in files:
    md = file.with_suffix(".md")
    td = str(file.parts[-1])[:2].upper() in ["TD", "TP"]
    if td:
        tds[file.parts[-2]].add(md)
    else:
        cours[file.parts[-2]] = str(md)
    md.write_text(template.render(pdf=str(file), size=8000 if td else 800, zoom="page-width" if td else "page-fit"))


def to_text(filename):
    return filename.replace("_", " ").replace("cor", "corrigé")

summary = Path("SUMMARY.md")
with summary.open("w") as f:
    f.write("# Summary\n\n")
    for section in cours:
        i = section.find("_")
        title = to_text(section[i+1:])
        f.write(f"- [{title[0].upper() + title[1:]}]({cours[section]})\n")
        for td in sorted(tds[section]):
            title = to_text(td.stem)
            f.write(f"\t- [{title[:2].upper() + title[2:]}]({td})\n")
