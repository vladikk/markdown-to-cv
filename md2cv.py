import codecs
import markdown2
import argparse
import sys
from subprocess import call
from jinja2 import Environment, PackageLoader

env = Environment(
    loader=PackageLoader('md2cv', 'templates')
)


def generate(source, target, template):
    with open(source, 'r') as md_file:
        md_text = md_file.read()

    html = markdown2.markdown(md_text, extras=["metadata"])

    template = env.get_template(template)

    params = {
        "html": html,
        "metadata": html.metadata
    }

    output_html = template.render(**params)
    html_file = "%s.html" % target
    pdf_file = "%s.pdf" % target

    with codecs.open(html_file, "w", "utf-8-sig") as output_file:
        output_file.write(output_html)

    cmd = "./pdf.sh %s %s" % (html_file, pdf_file)
    print(cmd)
    call(cmd, shell=True)


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        description='Markdown to CV (Html)',
        epilog="Example: python md2cv.py vladikk.md cv")

    parser.add_argument("md", help="Markdown CV file")
    parser.add_argument("output", help="Output file name")
    parser.add_argument("template", help="Template(in the templates directory")
    args = parser.parse_args()

    generate(source=args.md,
             target=args.output,
             template=args.template)

if __name__ == "__main__":
    main()
