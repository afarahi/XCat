from numpy                 import loadtxt
from XCat_Dictionary       import *
from XCat_tex_Introduction import Report_Introduction
from XCat_tex_Results      import Report_Results
from XCat_tex_Parameters   import Report_Parameters
from XCat_tex_bib          import Report_bib

def Report_File(Halo,Input,Output):
    import os
    import subprocess
    import shlex

    content= Report_title() \
            +Report_Introduction()\
            +Report_Results(Halo,Input,Output)\
            +Report_Parameters(Halo,Input,Output)\
            +Report_Acknowledgments()\
            +Report_bib()
 
    f1 = open('Report/report.tex','w')
    f1.write(content)
    f1.close


def Report_title():
    S = r'''\documentclass[12pt]{article}

\usepackage{amsmath}    % need for subequations
\usepackage{mathtools}  % need for math tools
\usepackage{amsmath}    % need for subequations
\usepackage{graphicx}   % need for figures
\usepackage{verbatim}   % useful for program listings
\usepackage{color}      % use if color is used in text
\usepackage{hyperref}   % use for hypertext links, including those to external documents and URLs
\usepackage{natbib}     % Used for Bibliography
\usepackage{ifthen}

% Names
\def\XCat{{\sc XCat}}

% Physical constants.
\def\G{{\rm G}}
\def\clight{{\rm c}}
\def\d{{\rm d}}
\def\e{{\rm e}}

% AdS
\newcounter{AdSDone}
\setcounter{AdSDone}{0}
\def\AdS{\ifthenelse{\equal{\arabic{AdSDone}}{0}}{anti de Sitter (AdS)\setcounter{AdSDone}{1}}{AdS}}

\title{\XCat\ Report}
\author{\copyright 2013 by Arya Farahi\thanks{E-mail: {\tt aryaf@umich.edu}}}
\date{\today}

\begin{document}
\maketitle

\begin{abstract}
In progress ...
\end{abstract}

'''
    return S



def Report_Acknowledgments():
    S = r'''
\section*{ACKNOWLEDGMENTS}
 Arya Farahi wants to thank ...
'''
    return S


