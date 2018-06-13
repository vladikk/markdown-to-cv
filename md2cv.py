import codecs
import markdown2
from jinja2 import Environment, PackageLoader

env = Environment(
    loader=PackageLoader('md2cv', 'templates')
)

with open('vladikk.md', 'r') as md_file:
    md_text = md_file.read()

html = markdown2.markdown(md_text, extras=["metadata"])

template = env.get_template('resume.html')

params = {
    "html": html,
    "metadata": html.metadata
}

output_html = template.render(**params)

with codecs.open("output.html", "w", "utf-8-sig") as output_file:
    output_file.write(output_html)
