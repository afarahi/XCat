from XCat_Utilities              import read_data_bool
from numpy                       import zeros, log10
from XCat_Objects                import DtoR
from matplotlib.pyplot           import *
from matplotlib                  import rc
import healpy                      as hp

rc('font',family='serif')

def plot_sky_projection_healpy_count(Sliced_Halo_data,nside):
    HEALPix_mode = read_data_bool(tag_name = 'HEALPix_Cartesian',file_name = 'parameters/Output_Parameters.xml')
    HEALPix_grat = read_data_bool(tag_name = 'HEALPix_Graticule',file_name = 'parameters/Output_Parameters.xml')
    fdir  = './Output/plots/HEALPix/'
    Sl_n  = len(Sliced_Halo_data)
    Z_max = max(Sliced_Halo_data[Sl_n-1].Z_red[:])
    rc('text',usetex=True)
    for k in range(Sl_n):
        pix     = zeros(12*nside**2)
        n       = len(Sliced_Halo_data[k].RA[:])
        for i in range(n):
           j    = hp.ang2pix(nside,DtoR*(90.0-Sliced_Halo_data[k].DEC[i]),DtoR*Sliced_Halo_data[k].RA[i])
           pix[j] += 1
        clf()
        if (HEALPix_mode):
           hp.cartview(pix)           
        else:
           hp.mollview(pix)
        if (HEALPix_grat):
           hp.graticule()
        fname = 'sky_projection_HEALPix_Count_%i_%i.pdf'%(nside,(k+1))
        title(r'sky projection for redshift between %0.2f and %0.2f'%(Sliced_Halo_data[k].z_min,Sliced_Halo_data[k].z_max),fontsize = 20)
        print 'Saving plot', fname
        savefig(fdir+fname,bbox_inches='tight')
    rc('text',usetex=False)  
    return 0


def plot_sky_projection_healpy_simple(Sliced_Halo_data,nside):
    HEALPix_mode = read_data_bool(tag_name = 'HEALPix_Cartesian',file_name = 'parameters/Output_Parameters.xml')
    HEALPix_grat = read_data_bool(tag_name = 'HEALPix_Graticule',file_name = 'parameters/Output_Parameters.xml')
    fdir  = './Output/plots/HEALPix/'
    Sl_n  = len(Sliced_Halo_data)
    Z_max = max(Sliced_Halo_data[Sl_n-1].Z_red[:])
    rc('text',usetex=True)
    for k in range(Sl_n):
        pix     = zeros(12*nside**2)
        n       = len(Sliced_Halo_data[k].RA[:])
        for i in range(n):
            j   = hp.ang2pix(nside,DtoR*(90.0-Sliced_Halo_data[k].DEC[i]),DtoR*Sliced_Halo_data[k].RA[i])
            pix[j] += 10.0**Sliced_Halo_data[k].lgFx[i]
        clf()
        if (HEALPix_mode):
           hp.cartview(pix)           
        else:
           hp.mollview(pix)
        if (HEALPix_grat):
           hp.graticule()
        fname = 'sky_projection_HEALPix_Simple_%i_%i.pdf'%(nside,(k+1))
        title(r'sky projection for redshift between %0.2f and %0.2f'%(Sliced_Halo_data[k].z_min,Sliced_Halo_data[k].z_max),fontsize = 20)
        print 'Saving plot', fname
        savefig(fdir+fname,bbox_inches='tight')
    rc('text',usetex=False)  

    return 0


def plot_sky_projection_healpy_all(Sliced_Halo_data,nside):
    plot_sky_projection_healpy_count(Sliced_Halo_data,nside)
    plot_sky_projection_healpy_simple(Sliced_Halo_data,nside)
    return 0


