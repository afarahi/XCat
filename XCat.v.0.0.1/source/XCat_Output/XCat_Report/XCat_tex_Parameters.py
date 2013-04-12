from numpy           import loadtxt
from XCat_Dictionary import *

def Report_Parameters(Halo,Input,Output):
    S = r''' 
\section{Parameters}

The following parameters are used in this run, \\

Cosmological Parameters:
\begin{verbatim}
  H_0      = ''' + str(Input.h_0) + r'''
  Omega_DE = ''' + str(Input.Omega_DE) + r'''
  Omega_m  = ''' + str(Input.Omega_M) + r'''
  Omega_b  = ''' + str(Input.Omega_b) + r'''
  Omega_r  = ''' + str(Input.Omega_R) + r'''
  Omega_k  = ''' + str(Input.Omega_k) + r'''
  w        = ''' + str(Input.w) + r'''
  sigma_8  = ''' + str(Input.sigma_8) + r'''
  ns       = ''' + str(Input.ns) + r'''
\end{verbatim}

'''
    return S

