import jinja2
from pathlib import Path

loader = jinja2.FileSystemLoader('.')
env = jinja2.Environment(loader=loader)

template = env.get_template("template_pdf.md")

for file in Path(".").rglob("*_*/**/*.pdf"):
    file.with_suffix(".md") \
        .write_text(template.render(pdf=str(file),
                                    zoom="page-width" if "TD" in str(file) else "page-fit"))
