"""
Find and print all variables provided for each template.

Script assumes that it is called from the top-level directory, i.e. using

$ python tools/templatevar.py
"""
import re
import numpy as np

exec(open("conf.py").read())

for template,d in templates.items():
    print( ("{template}\n"+"-"*len(template) ).format(template=template))
    text=open(d["template_file"]).read()
    
    vars=re.findall("\$.*?\$", text)
    # drop the $ delimiters
    vars=[var[1:-1] for var in vars]
    # drop all vars that begin with one of these strings
    dropstrings=["if(", "else", "sep", "for(", "end"]
    vars=[var for var in vars if np.all([not var.startswith(s) for s in dropstrings]) and len(var)>0]
    # get rid of duplicates and sort
    vars=sorted(set(vars))
    for var in vars:
        description=d["variables"][var] if var in d["variables"].keys() else ""
        print("- `{varname}`{sep}{description}".format(varname=var, 
            sep="" if len(description)==0 else ": ", 
            description=description))
    print("")
