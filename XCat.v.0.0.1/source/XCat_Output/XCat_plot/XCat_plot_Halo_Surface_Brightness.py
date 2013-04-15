from XCat_Utilities             import Read_Integer_Input, Read_YN_Input 
from numpy                      import log, log10, exp, sqrt, zeros
from matplotlib.pyplot          import *
from matplotlib                 import rc
import healpy                     as hp

def plot_Halo_Surface_Brightness(Halo_data,Input_Para,Output_Para):

    from XCat_Objects               import DtoR, RtoD
    rc('font',family='serif')
    fdir  = './Output/plots/HEALPixSurfaceBrightness/'

    nside = Output_Para.nside

    Sl_n  = len(Halo_data)
    k = Read_Integer_Input("We have %i redshift slice  which one you want exctract the halo ? "%Sl_n)
    k = int(k) - 1
    while(k > (Sl_n-1) or k < 0 ):
      print "Invalid Number."
      k = Read_Integer_Input("Please choose an integer between 1 and %i : "%Sl_n)
      k = int(k) - 1
    n       = len(Halo_data[k].RA[:])
    halo_n = Read_Integer_Input("We have %i halos in this slice which one you want to exctract ? "%n)
    halo_n = halo_n - 1
    d_l    = (Halo_data[k].X[halo_n]**2 + Halo_data[k].Y[halo_n]**2 + Halo_data[k].Z[halo_n]**2)

    from XCat_Objects               import Halo_Sample_Object
    Halo_Sample = Halo_Sample_Object(Halo_data[k],Input_Para,halo_n)

    pix     = zeros(12*nside**2)
    for i in range(len(Halo_Sample.sRA[:])):
       j    = hp.ang2pix(nside,DtoR*(90.0-Halo_Sample.sDEC[i]),DtoR*(Halo_Sample.sRA[i]))
       pix[j] += Halo_Sample.sSB[i]

    clf()
    hp.gnomview(pix, fig = 1 ,rot=(Halo_Sample.RA,Halo_Sample.DEC,0.0),xsize = Output_Para.xsize)
    hp.graticule()
    show()

    save_ques = Read_YN_Input("Do you want to save its picture (please enter Y, y, N, or n)? ")
    if save_ques :
      rc('text',usetex=True)
      clf()
      hp.gnomview(pix, fig = 1 ,rot=(Halo_Sample.RA,Halo_Sample.DEC,0.0),xsize = Output_Para.xsize)
      hp.graticule()
      fname = 'sky_projection_HEALPix_Surface_Brightness_Profile_%i_%i_%i.pdf'%(nside,(halo_n+1),(k+1))
      title(r'Surface Brightness Profile',fontsize = 20)
      print 'Saving plot', fname
#      savefig(fdir+fname,bbox_inches='tight')
      savefig(fdir+fname)
      rc('text',usetex=False)

