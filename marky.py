#!/usr/bin/python3
import sys
import mistune ## Library for converting .md to .html
import re
import click


def convert(m_file):
    
    ## Convert markdown to html
    markdown = mistune.Markdown()
    converted_md = markdown(m_file)
    return converted_md

def insert(cm_file, h_file, dest_file):
    
    ## Insert generated html code into html template
    final_doc = re.sub("<!-- Markdown Section -->", cm_file, h_file)
    
    ## Write to specified file
    new_file = open(dest_file, "w+")
    new_file.write(final_doc)
    new_file.close()

@click.command()
@click.argument('markdown', click.File('rb'), required=1)
@click.argument('template', click.File('rb'), required=1)
@click.argument('destination', click.File('w'), required=1)
def main(markdown, template, destination):

    ## Open files to read
    m_file = open(markdown, "r")
    h_file = open(template, "r")

    converted_md = convert(m_file.read())
    insert(converted_md, h_file.read(), destination)

    ## Close files after use
    m_file.close()
    h_file.close()

if __name__ == "__main__":
    main()
