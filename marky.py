#!/usr/bin/python3
import sys
import mistune ## Library for converting .md to .html
import re

## Convert markdown to html
md_file = open(sys.argv[1], "r")
markdown = mistune.Markdown()
converted_md = markdown(md_file.read())
md_file.close()

## Insert generated html code into html template
html_template = open(sys.argv[2], "r")
html_file = html_template.read()
final_doc = re.sub("<!-- Markdown Section -->", converted_md, html_file)
html_template.close()

## Write to specified file
new_file = open(sys.argv[3], "w+")
new_file.write(final_doc)
