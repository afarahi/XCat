from numpy                       import zeros, linspace, log10, savetxt, array
from XCat_Utilities              import Read_YN_Input
from XCat_Objects                import pi
from matplotlib                  import rc
import matplotlib.pyplot          as plt
#import healpy                     as hp

rc('font',family='serif')

def plot_logNlogS(Halo_data,Input_Para,Output_Para,General_Prop):

    from XCat_Objects               import DtoR, RtoD
    rc('font',family='serif')
    fdir  = './Output/plots/logN-logS/'

    nside = Output_Para.nside
    Sl_n  = len(Halo_data)

    tot_degree = General_Prop.total_sky_covered_deg2

    logS = linspace(-15.0,-10.0,41)
    S    = zeros(len(logS))
    N    = zeros(len(logS))

    for k in range(Sl_n):
       for i in range(len(Halo_data[k].RA[:])):
          for j in range(len(logS)):
             if (logS[j] <= Halo_data[k].lgFx[i]):
                N[j] += 1.0
    N = N/tot_degree
    S = 10.0**logS

    #Showing Plot
    plt.clf()
    plt.loglog(S,N)
    plt.show()

    #Saving Plot
    save_ques = Read_YN_Input("Do you want to save its picture (please enter Y, y, N, or n)? ")
    if save_ques :
      rc('text',usetex=True)
      plt.figure(1)
      plt.clf()
      fname = 'logN_logS_%i'%nside
      plt.loglog(S,N)
      plt.title(r'logN-logS',fontsize = 20)
      plt.xlabel(r'$S~(ergs/cm^2/s)~$in~$[0.5,2.0]~keV$',fontsize = 20)
      plt.ylabel(r'$N(>S)$~per~sq.deg',fontsize = 20)
      print 'Saving plot ', fname, '.pdf'
      plt.savefig(fdir+fname+'.pdf',bbox_inches='tight',dpi=200)
#      savefig(fdir+fname)
      rc('text',usetex=False)

      print 'Saving data ', fname, '.txt'
      f = open(fdir+fname+'.txt','w')
      f.write("#            S                  N\n")
      savetxt(f, array([S, N]).T)
      f.close()
    plt.close()
    del N, tot_degree, S, logS

    return 0
