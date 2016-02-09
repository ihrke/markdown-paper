# Scientific Papers in Markdown

The source of this document is written in [markdown](https://daringfireball.net/projects/markdown/) (file `paper.md`) and translated to latex using [pandoc](http://pandoc.org/) and customized templates located in the `templates` folder. References are stored in `references.bib` in [bibtex](http://www.bibtex.org/) format.

The `Makefile` details how the translation works. If you are on linux, simply calling `make` in the parent directory will compile the report to a pdf-format if all dependencies are installed. Edit the variables in the Makefile to choose a template (located in `./templates`).

So far, I have used it using `./templates/elsarticle-template-1.latex` but others may follow.

## Usage

1. Install the dependencies
    ~~~{bash}
sudo apt-get install pandoc pandoc-citeproc
pip install pandoc-fignos
    ~~~
2. Clone this repository
    ~~~{bash}
    git clone
    ~~~
3. Edit `Makefile` to choose a template
4. Write paper in `paper.md`, refs in `references.bib`, compile with `make`

NOTE: `paper.md` contains example code for tables, figures, equations, references and so on.

## Dependencies

- [pandoc](http://pandoc.org/)
- [pandoc-fignos](https://github.com/tomduck/pandoc-fignos)
- [pandoc-citeproc](https://github.com/jgm/pandoc-citeproc)
- a [latex](https://www.latex-project.org/)-distribution (e.g., [texlive](https://www.tug.org/texlive/)) including [bibtex](http://www.bibtex.org/)

---

Matthias Mittner <matthias.mittner@uit.no>
