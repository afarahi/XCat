from numpy           import loadtxt
from XCat_Dictionary import *

def Report_Results(Halo,Input,Output):
    S = r'''
\section{Results}
\subsection{Final Plots} 

'''
    if  Output.HEALPix_sky_proj:
      for i in range(len(Halo)):
         if (Output.HEALpix_mod == plot_sky_projection_healpy_count):
            S += r'''
\begin{figure}
  \centering
  \includegraphics[width=12cm]{./Output/plots/HEALPix/sky_projection_HEALPix_Count_''' + str(Output.nside) + r'''_''' + str(i+1) + r'''.pdf}
  \caption{Sky projection of halos number with redshit between ''' + str(Halo[i].z_min) + r''' and ''' + str(Halo[i].z_max) + r'''.}
  \label{fig:S-ProjCount-''' + str(i+1) + r'''}
\end{figure}

'''
         elif (Output.HEALpix_mod == plot_sky_projection_healpy_simple):
            S += r'''
\begin{figure}
  \centering
  \includegraphics[width=12cm]{./Output/plots/HEALPix/sky_projection_HEALPix_Simple_''' + str(Output.nside) + r'''_''' + str(i+1) + r'''.pdf}
  \caption{Sky projection of halos flux with redshit between ''' + str(Halo[i].z_min) + r''' and ''' + str(Halo[i].z_max) + r'''.}
  \label{fig:S-ProjSimple-''' + str(i+1) + r'''}
\end{figure}

'''
         elif (Output.HEALpix_mod == plot_sky_projection_healpy_all):
            S += r'''
\begin{figure}
  \centering
  \includegraphics[width=12cm]{./Output/plots/HEALPix/sky_projection_HEALPix_Count_''' + str(Output.nside) + r'''_''' + str(i+1) + r'''.pdf}
  \caption{Sky projection of halos number with redshit between ''' + str(Halo[i].z_min) + r''' and ''' + str(Halo[i].z_max) + r'''.}
  \label{fig:S-ProjCount-''' + str(i+1) + r'''}
\end{figure}

\begin{figure}
  \centering
  \includegraphics[width=12cm]{./Output/plots/HEALPix/sky_projection_HEALPix_Simple_''' + str(Output.nside) + r'''_''' + str(i+1) + r'''.pdf}
  \caption{Sky projection of halos flux with redshit between ''' + str(Halo[i].z_min) + r''' and ''' + str(Halo[i].z_max) + r'''.}
  \label{fig:S-ProjSimple-''' + str(i+1) + r'''}
\end{figure}
'''
    return S

