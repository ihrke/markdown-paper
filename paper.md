---
title:  'Great and certainly not overstated contribution to the literature'
journal: 'Journal of Good Research'
author:
- name: Me Ofcourse
  institute: Institute for Psychology, University of Tromsø
  email: me@myuni.no
  footnote: 1
- name: Some Otherdude
  footnote: 1
- name: And Thisguy
  footnote: 2
  corresponding: and.thisguy@otherplace.org
affiliation:
- number: 1
  name: Institute for Psychology, University of Tromsø
- number: 2
  name: University of Otherplace
keyword:
  - latex
  - markdown
abstract: |
  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
linenumbers: true
bibliography: references.bib
acknowledgements: |
  We'd like to thank bla bla and blablab
contribution: |
  Must include all authors, identified by initials, for example:
  A.A. conceived the experiment(s),  A.A. and B.A. conducted the experiment(s), C.A. and D.A. analysed the results.  All authors reviewed the manuscript.
additionalinformation: |
  To include, in this order: \textbf{Accession codes} (where applicable); \textbf{Competing financial interests} (mandatory statement).
  The corresponding author is responsible for submitting a \href{http://www.nature.com/srep/policies/index.html#competing}{competing financial interests statement} on behalf of all authors of the paper. This statement must be included in the submitted article file.
template: elsevier
documentclass_options: 
  - final
...

# Introduction

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Some [red text **which supports** markdown.]{.red}


<!---
Comments look like this and do not show up in the PDF
-->

References are cited as @mittner2014brain or [@mittner2014brain].

# Methods

- some
- bullet
- points

Footnotes can be entered using this code[^1].

[^1]: a footnote

Figures are included like this.

![This is gonna be the caption.](pics/dummy.pdf){#fig:dummy width=100%}

And referenced from here as Fig. @fig:dummy.

Complex tables can use standard LaTeX code as this one.

Equations can be used inline $y=\beta_0 + \beta_1 x + \epsilon$ or as usual $$f(x)=\frac{1}{x}$$

<!---
Table in LaTeX format because of fancy formatting
-->

\begin{table}[ht]
\centering
\caption{Probability to observe Bayes Factors of a certain magnitude or above for the used sample-size of $N=60$ assuming the original and the null-hypothesis.}
\begin{tabular}{llrrr}
  & & \multicolumn{3}{l}{$P(\text{BF}\ge\theta)$}\\
  Hypothesis & BF Type & $\theta=3$ & $\theta=10$ & $\theta=20$ \\
  \hline
  $d\sim \mathcal{N}(1.57, 0.51)$ & JZS BF$_{10}$ & 0.98 & 0.97 & 0.96 \\
     & Replication BF$_{10}$ & 0.98 & 0.96 & 0.96 \\
     & Meta-Analysis BF$_{10}$ & 0.99 & 0.99 & 0.99 \\\cline{2-5}
    $d=0$ & JZS BF$_{01}$ & 0.81 & 0.00 & 0.00 \\
   & Replication BF$_{01}$ & 0.98 & 0.95 & 0.91 \\
     & Meta-Analysis BF$_{01}$ & 0.63 & 0.27 & 0.06 \\
   \hline
\end{tabular}
\label{tab:probbf}
\end{table}

# Results

# Discussion

# References
