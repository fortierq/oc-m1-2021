import jinja2
from pathlib import Path
from collections import defaultdict

env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))

template = env.get_template("template_pdf.md")

tds = defaultdict(set)
cours = {}

for file in Path(".").rglob("*_*/**/*.pdf"):
    md = file.with_suffix(".md")
    if "TD" in str(file):
        tds[file.parts[-2]].add(md)
    else:
        cours[file.parts[-2]] = str(md)
    md.write_text(template.render(pdf=str(file), zoom="page-width" if "TD" in str(file) else "page-fit"))


def to_text(filename):
    return filename.replace("_", " ").title()


summary = Path("SUMMARY.md")
with summary.open("w") as f:
    for section in cours:
        i = section.find("_")
        f.write(f"- [{to_text(section[i+1:])}]({cours[section]})\n")
        for td in tds[section]:
            f.write(f"\t- [{to_text(td.stem)}]({td})\n")
