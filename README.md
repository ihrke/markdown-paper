# markdown-paper

Scientific paper in markdown using LaTeX. See the [pdf-directory](pdf/) for examples.

- [markdown-talk](https://github.com/ihrke/markdown-talk) - template for a beamer-based presentations
- [markdown-letter](https://github.com/ihrke/markdown-letter) - template for a letters
- [markdown-notes](https://github.com/ihrke/markdown-notes) - template for a notes

The source of this document is written in [markdown](https://daringfireball.net/projects/markdown/) (file `paper.md`) and translated to latex using [pandoc](http://pandoc.org/) and customized templates located in the `templates` folder. References are stored in `references.bib` in [bibtex](http://www.bibtex.org/) format.

The `Makefile.template` file details how the translation works. 

There is a convenience script `build.py` that creates a `Makefile` from `Makefile.template` that is consistent with the desired template as specified in the `template` field in the markdown-header. All supported templates are listed in `conf.py`.  Which template to use is specified in the header of the `.md`-file using the `template:` field. If the template is not changed, `build.py` does not need to be rerun but simply calling `make` will suffice. It is also possible to specify the desired template on the command-line using the `-t <template name>` option. See `python build.py -h` for details. Note, however, that not all variables are implemented for all templates.

If you are on linux, simply calling `make` in the parent directory will compile the report to a pdf-format if all dependencies are installed.

## Preview of templates

![paper_elife](pics/paper_elife.png)
![paper_elsevier](pics/paper_elsevier.png)
![paper_generic](pics/paper_generic.png)
![paper_scientific_reports](pics/paper_scientific_reports.png)
![paper_springer](pics/paper_springer.png)
![paper_wiley](pics/paper_wiley.png)

## Supported templates

This is a list of all supported templates along with a list of all variables defined for each template. It is generated using `tools/templatevar.py` and may or may not be outdated.

elife
-----
- `abstract`
- `acknowledgements`
- `additionalinformation`
- `affiliation.name`
- `affiliation.number`
- `author.email`
- `author.footnote`
- `author.name`
- `author.orcid`
- `bibliography`
- `body`
- `contribution`
- `data`
- `funding`
- `shorttitle`
- `title`

elsevier
--------
- `abstract`
- `acknowledgements`
- `additionalinformation`
- `affiliation`
- `affiliation.name`
- `affiliation.number`
- `author-meta`
- `author.address`
- `author.email`
- `author.footnote`
- `author.name`
- `bibliography`
- `body`
- `citecolor`
- `contribution`
- `journal`: journal name (str)
- `keyword`
- `linkcolor`
- `title`
- `title-meta`
- `toc-depth`
- `urlcolor`

scientific_reports
------------------
- `abstract`
- `acknowledgements`
- `additionalinformation`
- `affiliation.name`
- `affiliation.number`
- `author.email`
- `author.footnote`
- `author.name`
- `bibliography`
- `body`
- `contribution`
- `keyword`
- `title`

springer
--------
- `abstract`
- `acknowledgements`
- `additionalinformation`
- `author.email`
- `author.footnote`
- `author.institute`
- `author.name`
- `bibliography`
- `body`
- `documentclass_options`
- `journal`
- `keyword`
- `svjourstyle`
- `title`
- `toc-depth`

wiley
-----
- `abbreviation`
- `abstract`
- `acknowledgements`
- `additionalinformation`
- `affiliation.name`
- `affiliation.number`
- `author`
- `author.email`
- `author.footnote`
- `author.institute`
- `author.name`
- `bibliography`
- `body`
- `contribution`
- `funding`
- `journalsection`
- `keyword`
- `papertype`
- `title`

## Installation

### first you need `LateX`

~~~{bash}
brew install --cask mactex-no-gui
~~~
then add `export PATH=$PATH:/Library/TeX/texbin` to your .*rc and source it


### with `conda`

~~~{bash}
conda create --name testenv pandoc pandocfilters
conda activate testenv
pip install pandoc-fignos
~~~

### linux

~~~{bash}
sudo apt-get install pandoc pandoc-citeproc
pip install pandoc-fignos
~~~


## Usage

1. Clone this repository

    ~~~{bash}
    git clone
    ~~~
2. Write paper in `paper.md`, refs in `references.bib`
3. compile with `python build.py paper.md`

~~~
usage: build.py [-h] [-t TEMPLATE] [-b] mdfile

positional arguments:
  mdfile

optional arguments:
  -h, --help            show this help message and exit
  -t TEMPLATE, --template TEMPLATE
                        template to use for translation
  -b, --build-makefile-only
                        build Makefile only or also run latex?
~~~

NOTE: `paper.md` contains example code for tables, figures, equations, references and so on.


## Dependencies

- [pandoc](http://pandoc.org/)
- [pandoc-fignos](https://github.com/tomduck/pandoc-fignos)
- [pandoc-citeproc](https://github.com/jgm/pandoc-citeproc)
- a [latex](https://www.latex-project.org/)-distribution (e.g., [texlive](https://www.tug.org/texlive/)) including [bibtex](http://www.bibtex.org/)

---

Matthias Mittner <matthias.mittner@uit.no>
