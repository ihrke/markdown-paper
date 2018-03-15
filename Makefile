PAPER=paper
BIBLIOGRAPHY=references.bib
#TEMPLATE=templates/elsarticle-template-1-num.latex
TEMPLATE=templates/scientific_reports.latex
PANDOC=pandoc
USE_NATBIB=--biblatex #--natbib

export TEXINPUTS=.:./templates/dependencies//:
export BIBINPUTS=.:./templates/dependencies//:


${PAPER}.pdf: ${PAPER}.tex ${BIBLIOGRAPHY}
	pdflatex ${PAPER}.tex
	bibtex ${PAPER}
	pdflatex ${PAPER}.tex

${PAPER}.tex: ${PAPER}.md ${BIBLIOGRAPHY} ${TEMPLATE}
	${PANDOC} -s -S --filter pandoc-fignos --filter pandoc-citeproc ${USE_NATBIB} ${PAPER}.md -o ${PAPER}.tex --template ${TEMPLATE} --bibliography ${BIBLIOGRAPHY}

watch: $(MD_FILES) $(BIBLIOGRAPHY)
	fswatch -o $^ | xargs -n1 -I{} make
