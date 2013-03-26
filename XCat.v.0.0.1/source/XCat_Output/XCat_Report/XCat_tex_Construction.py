from numpy           import loadtxt
from XCat_Dictionary import *

def Report_File(Halo,Input,Output):
    import os
    import subprocess
    import shlex

    content= Report_title() \
            +Report_introduction()\
            +Report_Reuslts(Halo,Input,Output)\
            +Report_parameters(Halo,Input,Output)\
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


def Report_introduction():
    S = r'''
\section{Introduction}

\XCat\ is an open source code for data analysing of X-Ray observational data of variouse fields in AdS spaces. It is developed in 2013 by Arya Farahi for ... project under guidance of August E. Evrard at University of Michigan - Ann Arbor. '''
    return S


def Report_Reuslts(Halo,Input,Output):
    S = r''' '''
    if  Output.HEALPix_sky_proj:
      if (Output.HEALpix_mod == plot_sky_projection_healpy_count):
         S += r'''
\section{Results}
\subsection{Final Plots}

\begin{figure}[hbt]
 \centering
 \includegraphics[width=12cm]{./Output/plots/HEALPix/sky_projection_HEALPix_Count_''' + str(Output.nside) + r'''.pdf}
 \caption{Plot of sky projection.}
 \label{fig:S-ProjCount}
\end{figure}

'''
      elif (Output.HEALpix_mod == plot_sky_projection_healpy_simple):
         S += r'''
\section{Results}
\subsection{Final Plots}

\begin{figure}[hbt]
 \centering
 \includegraphics[width=12cm]{./Output/plots/HEALPix/sky_projection_HEALPix_Simple_''' + str(Output.nside) + r'''.pdf}
 \caption{Plot of sky projection.}
 \label{fig:S-ProjSimple}
\end{figure}
'''
      elif (Output.HEALpix_mod == plot_sky_projection_healpy_all):
         S += r'''
\section{Results}
\subsection{Final Plots}

\begin{figure}[hbt]
 \centering
 \includegraphics[width=12cm]{./Output/plots/HEALPix/sky_projection_HEALPix_Count_''' + str(Output.nside) + r'''.pdf}
 \caption{Plot of sky projection.}
 \label{fig:S-ProjCount}
\end{figure}

\begin{figure}[hbt]
 \centering
 \includegraphics[width=12cm]{./Output/plots/HEALPix/sky_projection_HEALPix_Simple_''' + str(Output.nside) + r'''.pdf}
 \caption{Plot of sky projection.}
 \label{fig:S-ProjSimple}
\end{figure}
'''

    return S


def Report_parameters(Halo,Input,Output):
    S = r''' .... '''
    return S

def Report_Acknowledgments():
    S = r'''
\section*{ACKNOWLEDGMENTS}
 Arya Farahi wants to thank ...
'''
    return S


def Report_bib():
    S = r''' 
\end{document}
'''
    return S
