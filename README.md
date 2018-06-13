# Markdown to CV

A simple python script that parses markdown files and generates CV files.

## Usage

The following command generates "cv.html" file from vladikk.md, using the "resume.html" template:

python md2cv.py vladikk.md cv resume.html

## Input Schema

See the vladikk.md for a reference markdown document.

Note: Markdown's horizontal rule("---") is used for denoting page breaks, when the resulting CV file is printed.

## Requirements

* python 2.7
* requirements.txt
* Docker - for generation of PDF files via the "openlabs/docker-wkhtmltopdf" image