import os
import sys
import re
import json
from subprocess import Popen, PIPE
from pandocfilters import stringify

import argparse

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("mdfile")
ap.add_argument("-t", "--template", required=False, help="template to use for translation")
ap.add_argument("-b", "--build-makefile-only", action="store_true", required=False, help="build Makefile only or also run latex?", default=False)
args = vars(ap.parse_args())

## read conf.py which has all supported templates
exec(open("conf.py").read())

mdfile=args["mdfile"]

## convert md to JSON
process = Popen(["pandoc", "-t", "json", mdfile], stdout=PIPE)
(output, err) = process.communicate()
exit_code = process.wait()
mdjson=json.loads(output)

## get target template
if args["template"] is not None: ## command-line arg has priority
  target_template=args["template"]
elif "template" not in mdjson["meta"]:
  print("WARN: no template found in header, using default '%s'"%default_template)
  target_template=default_template
else:
  target_template=stringify(mdjson["meta"]["template"])

if target_template not in templates.keys():
  print("WARN: template '%s' found in header not know, falling back to '%s'"%(target_template, default_template))
  target_template=default_template
print("> using template '%s'"%target_template)

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
  
if not args["build_makefile_only"]:
  os.system("make clean")
  os.system("make")
