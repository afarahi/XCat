from numpy                       import zeros, log10
from XCat_Objects                import DtoR
from matplotlib.pyplot           import *
from matplotlib                  import rc
import healpy                      as hp

rc('font',family='serif')

def plot_sky_projection_healpy_count(Halo_data,nside):

    n = Halo_data.number_of_halos
    Z_max = max(Halo_data.Z_red)
    
    pix = zeros(12*nside**2)
    
    for i in range(n):
#       j = hp.ang2pix(nside,DtoR*Halo_data.gLong[i],DtoR*Halo_data.gLati[i])
       j = hp.ang2pix(nside,DtoR*(90.0-Halo_data.DEC[i]),DtoR*(180.0+Halo_data.RA[i]))
       pix[j] += 1

    hp.mollview(pix)

    fdir  = './Output/plots/HEALPix/'
    fname = 'sky_projection_HEALPix_Count_%i.pdf'%nside
    rc('text',usetex=True)
    title(r'sky projection',fontsize = 20)
    print 'Saving plot', fname
    savefig(fdir+fname)
    rc('text',usetex=False)  

    return 0


def plot_sky_projection_healpy_simple(Halo_data,nside):

    n = Halo_data.number_of_halos
    
    pix = zeros(12*nside**2)
    
    for i in range(n):
#       j = hp.ang2pix(nside,DtoR*Halo_data.gLong[i],DtoR*Halo_data.gLati[i])
       j = hp.ang2pix(nside,DtoR*(90.0-Halo_data.DEC[i]),DtoR*(180.0+Halo_data.RA[i]))
       pix[j] += 10.0**Halo_data.lgFx[i]
#       print pix[j],Halo_data.lgFx[i]
      
    hp.mollview(pix)
    
    fdir  = './Output/plots/HEALPix/'
    fname = 'sky_projection_HEALPix_Simple_%i.pdf'%nside
    rc('text',usetex=True)
    title(r'sky projection',fontsize = 20)
    print 'Saving plot', fname
    savefig(fdir+fname)
    rc('text',usetex=False)

    return 0


def plot_sky_projection_healpy_all(Halo_data,nside):
    plot_sky_projection_healpy_count(Halo_data,nside)
    plot_sky_projection_healpy_simple(Halo_data,nside)
    return 0


