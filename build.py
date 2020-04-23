import os
import sys
import re
import json
from subprocess import Popen, PIPE
from pandocfilters import stringify

default_template="elsevier"
templates={
  "elsevier":{
    "template_file":"templates/elsarticle-template-1-num.latex",
    "bibtexcommand":"bibtex",
    "natbib":"--natbib"
    },
  "scientific_reports":{
    "template_file":"templates/scientific_reports.latex",
    "bibtexcommand":"biber",
    "natbib":"--biblatex"
    },
  "springer":{
    "template_file":"templates/springer_svjour3.latex",
    "bibtexcommand":"bibtex",
    "natbib":"--natbib"
    }
  }

mdfile=sys.argv[1]

## convert md to JSON
process = Popen(["pandoc", "-t", "json", mdfile], stdout=PIPE)
(output, err) = process.communicate()
exit_code = process.wait()
mdjson=json.loads(output)

## get target template
if "template" not in mdjson["meta"]:
  print("WARN: no template found in header, using default '%s'"%default_template)
  target_template=default_template
else:
  target_template=stringify(mdjson["meta"]["template"])
  if target_template not in templates.keys():
    print("WARN: template '%s' found in header not know, falling back to '%s'"%(target_template, default_template))
    target_template=default_template

if "bibliography" not in mdjson["meta"]:
  print("ERROR: no bibliography found in md-header")
  sys.exit()
bibtexfile=stringify(mdjson["meta"]["bibliography"])

config=templates[target_template]
config["mdfile"]=os.path.splitext(mdfile)[0]
config["bibtexfile"]=bibtexfile

with open("Makefile.template", "r") as f:
  mktext=f.read()

mktext=mktext.format(**config)
with open("Makefile", "w") as f:
  f.write(mktext)
  
os.system("make clean")
os.system("make")
