#!/usr/bin/env python

"""
Pandoc filter to enable coloring text by using bracket_span syntax.
I.e., 

> This is not highlighted but [this is!]{.red} 

will result in 

> This is not highlighted but \textcolor{red}{this is!}

when translated to latex.

Adapted from https://github.com/jgm/pandocfilters/blob/master/examples/latexdivs.py.
"""

from pandocfilters import toJSONFilter, RawBlock, RawInline, stringify
import sys


def latex(x):
    return RawInline('latex', x)

def latexdivs(key, value, format, meta):
    if key == 'Span':
        #print >>sys.stderr,key,value,format,meta
        [[ident, classes, kvs], contents] = value
        #print >>sys.stderr,ident,classes,kvs,contents
        if "red" in classes:
            if format == "latex":
                #print >>sys.stderr,"HALLO"
                if ident == "":
                    label = ""
                else:
                    label = '\\label{' + ident + '}'
                #print >>sys.stderr, [latex('\\textcolor{red}{' + stringify(contents) + '}')]
                return([latex('\\textcolor{red}{')] + contents + [latex('}')])

if __name__ == "__main__":
    toJSONFilter(latexdivs)
