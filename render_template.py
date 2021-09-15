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
    td = "TD" in str(file)
    if td:
        tds[file.parts[-2]].add(md)
    else:
        cours[file.parts[-2]] = str(md)
    md.write_text(template.render(pdf=str(file), size=8000 if td else 800, zoom="page-width" if td else "page-fit"))


def to_text(filename):
    return filename.replace("_", " ").title()


summary = Path("SUMMARY.md")
with summary.open("w") as f:
    f.write("# Summary\n\n")
    for section in cours:
        f.write(f"- [{to_text(section)}]({cours[section]})\n")
        for td in tds[section]:
            f.write(f"\t- [{to_text(td.stem)}]({td})\n")
