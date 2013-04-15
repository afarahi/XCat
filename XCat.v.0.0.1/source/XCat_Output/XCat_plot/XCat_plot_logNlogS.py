from numpy                       import zeros, linspace, log10
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
#    pix     = zeros(12*nside**2)

#    for k in range(Sl_n):
#       for i in range(len(Halo_data[k].RA[:])):
#          n       = len(Halo_data[k].RA[:])
#          j       = hp.ang2pix(nside,DtoR*(90.0-Halo_data[k].DEC[i]),DtoR*(Halo_data[k].RA[i]))
#          pix[j] += 1

#    tot_pix = 0
#    for i in range(len(pix)):
#      if (pix[i] != 0):
#         tot_pix += 1

    tot_degree = General_Prop.total_sky_covered_deg2
#    print tot_degree
#    tot_degree = 360.0*180.0*float(tot_pix)/float(len(pix))
#    print tot_degree

#    del pix, tot_pix

    logS   = linspace(-15.0,-10.0,21)
    N_cond = zeros(len(logS))

    print logS

    for k in range(Sl_n):
       for i in range(len(Halo_data[k].RA[:])):
          if ( Halo_data[k].lgFx[i] < logS[0] ):
             N_cond[0] += 1
          else:
             for j in range(1,len(logS)):
                if ( (logS[j-1] <= Halo_data[k].lgFx[i]) and (Halo_data[k].lgFx[i] < logS[j])):
                   N_cond[j] += 1
                   break
   
    N = zeros(len(logS))
    S = zeros(len(logS))

    for i in range(len(logS)):
       for j in range(1,i+1):
          N[len(logS)-i-1] += float(N_cond[len(logS)-j])
       N[i] = N[i]/tot_degree
       S[i] = 10.0**logS[i]
 
    del N_cond, tot_degree

    print S
    print N
    #Showing Plot
    plt.clf()
    plt.loglog(S[1:len(logS)-1],N[1:len(logS)-1])
    plt.show()

    #Saving Plot
    save_ques = Read_YN_Input("Do you want to save its picture (please enter Y, y, N, or n)? ")
    if save_ques :
      rc('text',usetex=True)
      plt.clf()
      fname = 'logN_logS_%i.pdf'%nside
      plt.loglog(10.0**logS,N)
      plt.title(r'logN-logS',fontsize = 20)
      plt.xlabel(r'$S~(ergs/cm^2/s)~$in~$[0.5,2.0]~keV$',fontsize = 20)
      plt.ylabel(r'$N(>S)$~per~sq.deg',fontsize = 20)
      print 'Saving plot', fname
      plt.savefig(fdir+fname,bbox_inches='tight',dpi=200)
#      savefig(fdir+fname)
      rc('text',usetex=False)


    return 0
