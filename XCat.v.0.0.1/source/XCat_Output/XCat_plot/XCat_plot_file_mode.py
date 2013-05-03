from XCat_Utilities             import Read_Integer_Input, Read_YN_Input, Read_String_Input, Read_Float_Input
from numpy                      import loadtxt, sqrt, floor
from matplotlib                 import rc
import matplotlib.pyplot          as plt
import healpy                     as hp

def isnpixok(npix):
    nside = sqrt(float(len(npix))/12.0)
    return (nside == floor(nside))

def load_map_file():
    import os.path
    fdir  = Read_String_Input("Please enter directory of map file (e.g. ./Output/) : ")
    if (not os.path.exists(fdir)):
       print "There is not folder with this address."
       raw_input("Press enter to continue ... ")
       return (False,0)
    fname = Read_String_Input("Please enter name of map file (e.g. map.txt) : ")
    if (not os.path.isfile(fdir+fname)):
       print "There is not file with this name."
       raw_input("Press enter to continue ... ")
       return (False,0)
    try: 
       print "\n Loading ... \n"
       pix = loadtxt(fdir+fname, comments='#', unpack=True)
    except (TypeError, ValueError): 
       print " Can not read the file."
       raw_input("Press enter to continue ... ")
       return (False,0)
    if (isnpixok(pix)):
       return (True,pix)
    else:
       print fname , " is not a HEALPix map file ."
       raw_input("Press enter to continue ... ")
       return (False,0)


def plot_full_sky_normal(Output_Para,pix,pix_bool):
    rc('font',family='serif')
    if (pix_bool):
       plt.clf()
       hp.mollview(pix, fig = 1)
       hp.graticule()
       plt.show()
       plt.close()
    else:
       print "Please, first load a HEALPix map file ."
       raw_input("Press enter to continue ... ")
       return 0
    save_ques = Read_YN_Input("Do you want to save its picture (please enter Y, y, N, or n)? ")
    if save_ques :
       rc('text',usetex=True)
       plt.clf()
       hp.mollview(pix, fig = 1)
       hp.graticule()
       print 'Saving plot', fname
       plt.savefig(fdir+fname+'_moll.pdf',bbox_inches='tight')
#       plt.savefig(fdir+fname+'.pdf')
       rc('text',usetex=False)
       plt.close()

def plot_full_sky_cart(Output_Para,pix,pix_bool):
    rc('font',family='serif')
    if (pix_bool):
       plt.clf()
       hp.cartview(pix, fig = 1)
       hp.graticule()
       plt.show()
       plt.close()
    else:
       print "Please, first load a HEALPix map file ."
       raw_input("Press enter to continue ... ")
       return 0
    save_ques = Read_YN_Input("Do you want to save its picture (please enter Y, y, N, or n)? ")
    if save_ques :
       rc('text',usetex=True)
       plt.clf()
       hp.cartview(pix, fig = 1)
       hp.graticule()
       print 'Saving plot', fname
       plt.savefig(fdir+fname+'_cart.pdf',bbox_inches='tight')
#       plt.savefig(fdir+fname+'.pdf')
       rc('text',usetex=False)
       plt.close()

def plot_zoom_sky(Output_Para,pix,pix_bool):
    rc('font',family='serif')
    from XCat_Objects import DtoR
    if (pix_bool):
       lon = Read_Float_Input("Please enter long (-180<long<180) : ")
       lat = Read_Float_Input("Please enter lati (-90<long<90) : ")
       rot = Read_Float_Input("Please enter rot (0<rot<360) : ")
       res = Read_Float_Input("Please enter resolution (in arcmin) : ")
    else:
       print "Please, first load a HEALPix map file ."
       raw_input("Press enter to continue ... ")
       return 0


    plt.clf()
    hp.gnomview(pix, fig = 1, rot=(lon,lat,rot),reso = res)
    hp.graticule()
    plt.show()
    plt.close()

    save_ques = Read_YN_Input("Do you want to save its picture (please enter Y, y, N, or n)? ")
    if save_ques :
       rc('text',usetex=True)
       plt.clf()
       hp.gnomview(pix, fig = 1, rot=(lon,lat,rot),reso = res)
       hp.graticule()
       print 'Saving plot', fname
       plt.savefig(fdir+fname+'_zoom.pdf',bbox_inches='tight')
#       plt.savefig(fdir+fname+'.pdf')
       rc('text',usetex=False)
       plt.close()
