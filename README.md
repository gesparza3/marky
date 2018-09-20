# marky
A command line tool for inserting markdown files into html templates
****

## About
`marky` is a command-line tool written in Python to make it easy to embed Markdown documents into an html page. The user must have a html template so that `marky` can place the contents of the Markdown file into a new html file. In order to make sure your template is compatible, place `<!-- Markdown section -->` in the template.

### Example:

```
<div class="container">
    <article class="markdown-body">
          <!-- Markdown Section --> 
    </article>
 </div>
```

When ran, the tool will convert the markdown document to html and then insert the contents into a new html file based on the template.

## Dependencies
It is recommended you install [pipsi](https://github.com/mitsuhiko/pipsi) to ensure there are no version conflicts with other programs.

## Installation

To install this tool, clone this repository:
```
git clone https://github.com/gesparza3/marky
```
Navigate into the remote repository and into the folder `marky`:
```
cd marky/marky
```

Then run the following command:
```
pipsi install .
```

## Usage
```
marky --help
```
