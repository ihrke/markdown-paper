default_template="elsevier"
templates={
  "elsevier":{
    "template_file":"templates/elsarticle-template-1-num.latex",
    "bibtexcommand":"bibtex",
    "natbib":"--natbib",
    "variables":{ ## specify/document variables 
        "journal":"journal name (str)"
    }
    },
  "scientific_reports":{
    "template_file":"templates/scientific_reports.latex",
    "bibtexcommand":"biber",
    "natbib":"--biblatex",
    "variables":{ ## specify/document variables 

    }
    },
  "springer":{
    "template_file":"templates/springer_svjour3.latex",
    "bibtexcommand":"bibtex",
    "natbib":"--natbib",
    "variables":{ ## specify/document variables 

    }
    }
  }
