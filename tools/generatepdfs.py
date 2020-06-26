"""
Generate PDFs for all supported templates and store them in `pdf/`.
Script assumes that it is called from the top-level directory, i.e. using

$ python tools/generatepdfs.py
"""
import os
os.makedirs("pdf", exist_ok=True) 

import argparse
# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("mdfile")
ap.add_argument("-d", "--dry-run", action="store_true", default=False, required=False, help="only output commands to run")
args = vars(ap.parse_args())
mdfile=args["mdfile"]

## read conf.py which has all supported templates
exec(open("conf.py").read())

for template,d in templates.items():
    print("> {template}".format(template=template) )
    cmdstr="python build.py -t {template} {mdfile}".format(template=template, mdfile=mdfile)
    print(">",cmdstr)
    if not args["dry_run"]:
        os.system(cmdstr)
    cmdstr="cp {fname}.pdf pdf/{fname}_{template}.pdf".format(fname=os.path.splitext(mdfile)[0],template=template)
    print(">",cmdstr)
    if not args["dry_run"]:
        os.system(cmdstr)

## clean up
cmdstr="make clean"
print(">",cmdstr)
if not args["dry_run"]:
    os.system(cmdstr)