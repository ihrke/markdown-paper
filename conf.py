default_template="elsevier"
templates={
  "elife":{
    "template_file":"templates/lapreprint-elife.latex",
    "bibtexcommand":"bibtex",
    "natbib":"--natbib",
    "variables":{ ## specify/document variables 

    }
  },
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
    },
  "wiley":{
      "template_file":"templates/wiley.latex",
      "bibtexcommand":"bibtex",
      "natbib":"--natbib",
      "variables":{

      }
  },
  "generic":{
    "template_file":"templates/paper.latex",
      "bibtexcommand":"biber",
      "natbib":"--biblatex",
      "variables":{

      }
  }
  }
