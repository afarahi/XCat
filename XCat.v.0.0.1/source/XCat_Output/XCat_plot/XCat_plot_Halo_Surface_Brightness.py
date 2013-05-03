from XCat_Utilities             import Read_Integer_Input, Read_YN_Input 
from XCat_Objects               import pi
from numpy                      import log, log10, exp, sqrt, zeros, savetxt, array
from matplotlib                 import rc
import matplotlib.pyplot          as plt
import healpy                     as hp

def plot_Single_Halo_Surface_Brightness(Halo_data,Input_Para,Output_Para):

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
    if (n == 0):
       print "There is no halo in this piece of redshift, please choos another one ..."
       raw_input("Press enter to continue ... ")
       return 

    halo_n = Read_Integer_Input("We have %i halos in this slice which one you want to exctract ? "%n)
    halo_n = halo_n - 1

    from XCat_Objects               import Halo_Brightness_Surface_Sample_Object
    Halo_Sample = Halo_Brightness_Surface_Sample_Object(Halo_data[k],Input_Para,Output_Para,halo_n)

    pix     = zeros(12*nside**2)
    for i in range(len(Halo_Sample.sRA[:])):
       j    = hp.ang2pix(nside,DtoR*(90.0-Halo_Sample.sDEC[i]),DtoR*(Halo_Sample.sRA[i]))
       pix[j] += Halo_Sample.sSB[i]
    if (Output_Para.log_scale):
       pix_min = max(pix[:])/10.0**4
       pix = log10((pix+pix_min)*4.0*pi/(12.0*nside**2))
    else:
       pix = pix/(12.0*nside**2)
    plt.clf()
    hp.gnomview(pix, fig=1 ,rot=(Halo_Sample.RA,Halo_Sample.DEC,0.0), xsize=Output_Para.xsize , reso=Output_Para.resolution , degree=Output_Para.resol_degree)
    hp.graticule()
    plt.show()
    plt.close()

    save_ques = Read_YN_Input("Do you want to save its picture (please enter Y, y, N, or n)? ")
    if save_ques :
      rc('text',usetex=True)
      plt.clf()
      hp.gnomview(pix, fig=1 , rot=(Halo_Sample.RA,Halo_Sample.DEC,0.0) , xsize=Output_Para.xsize , reso=Output_Para.resolution , degree=Output_Para.resol_degree)
      hp.graticule()
      if (Output_Para.log_scale):
        fname = 'sky_projection_HEALPix_Surface_Brightness_Profile_log_%i_%i_%i.pdf'%(nside,(halo_n+1),(k+1))
      else:
        fname = 'sky_projection_HEALPix_Surface_Brightness_Profile_%i_%i_%i.pdf'%(nside,(halo_n+1),(k+1))
      plt.title(r'Surface Brightness Profile',fontsize = 20)
      print 'Saving plot', fname
#      savefig(fdir+fname,bbox_inches='tight')
      plt.savefig(fdir+fname)
      rc('text',usetex=False)
      plt.close()

def plot_Pixel_Halos_Surface_Brightness(Halo_data,Input_Para,Output_Para):

    from XCat_Objects               import DtoR, RtoD
    rc('font',family='serif')
    fdir  = './Output/plots/HEALPixSurfaceBrightness/'

    nside = Output_Para.nside

    Sl_n  = len(Halo_data)

    from XCat_Objects  import Halo_Brightness_Surface_Sample_Object

    for k in range(Sl_n):

      pix     = zeros(12*nside**2)

      if (len(Halo_data[k].RA[:]) == 0):
         pass 
      else:
         for halo_n in range(len(Halo_data[k].RA[:])):
            Halo_Sample     = Halo_Brightness_Surface_Sample_Object(Halo_data[k],Input_Para,Output_Para,halo_n)
            for i in range(len(Halo_Sample.sRA[:])):
               j    = hp.ang2pix(nside,DtoR*(90.0-Halo_Sample.sDEC[i]),DtoR*(Halo_Sample.sRA[i]))
               pix[j] += Halo_Sample.sSB[i]
         if (Output_Para.log_scale):
            pix_min = max(pix[:])/10.0**4
            pix = log10((pix+pix_min)*4.0*pi/(12.0*nside**2))
         else:
            pix = pix/(12.0*nside**2)
         plt.clf()
         hp.gnomview(pix, fig=1 , rot=(Halo_Sample.RA,Halo_Sample.DEC,0.0) , xsize=Output_Para.xsize , reso=Output_Para.resolution , degree=Output_Para.resol_degree)
         hp.graticule()
         plt.show()
         plt.close()

         save_ques = Read_YN_Input("Do you want to save the plot (please enter Y, y, N, or n)? ")
         if save_ques :
           rc('text',usetex=True)
           plt.clf()
           hp.gnomview(pix, fig = 1 ,rot=(Halo_Sample.RA,Halo_Sample.DEC,0.0),xsize = Output_Para.xsize)
           hp.graticule()
           if (Output_Para.log_scale):
              fname = 'Surface_Brightness_Profile_log_%i_%i.pdf'%(nside,(k+1))
           else:
              fname = 'Surface_Brightness_Profile_%i_%i.pdf'%(nside,(k+1))
           plt.title(r'Surface Brightness Profile at redshift between %0.3f and %0.3f'%(Halo_data[k].z_min,Halo_data[k].z_max),fontsize = 20)
           print 'Saving plot', fname
#         savefig(fdir+fname,bbox_inches='tight')
           plt.savefig(fdir+fname)
           rc('text',usetex=False)
           plt.close()

         save_ques = Read_YN_Input("Do you want to save the map data (please enter Y, y, N, or n)? ")
         if save_ques :
           if (Output_Para.log_scale):
              fname = 'Surface_Brightness_Profile_log_HEALPix_map_%i_%i.txt'%(nside,(k+1))
           else:
              fname = 'Surface_Brightness_Profile_HEALPix_map_%i_%i.txt'%(nside,(k+1))
           print 'Saving data', fname
           f = open(fdir+fname,'w')
           f.write("#   Pix_Value \n")
           savetxt(f, array([pix]).T)
           f.close()

def plot_Total_Sky_Halos_Surface_Brightness(Halo_data,Input_Para,Output_Para):

    from XCat_Objects               import DtoR, RtoD
    rc('font',family='serif')
    fdir  = './Output/plots/HEALPixSurfaceBrightness/'

    nside = Output_Para.nside

    Sl_n  = len(Halo_data)

    from XCat_Objects               import Halo_Brightness_Surface_Sample_Object

    for k in range(Sl_n):

      pix     = zeros(12*nside**2)

      if (len(Halo_data[k].RA[:]) == 0):
         pass 
      else:
         for halo_n in range(len(Halo_data[k].RA[:])):
            Halo_Sample     = Halo_Brightness_Surface_Sample_Object(Halo_data[k],Input_Para,Output_Para,halo_n)
            for i in range(len(Halo_Sample.sRA[:])):
               j    = hp.ang2pix(nside,DtoR*(90.0-Halo_Sample.sDEC[i]),DtoR*(Halo_Sample.sRA[i]))
               pix[j] += Halo_Sample.sSB[i]
         if (Output_Para.log_scale):
            pix_min = max(pix[:])/10.0**4
            pix = log10((pix+pix_min)*4.0*pi/(12.0*nside**2))
         else:
            pix = pix/(12.0*nside**2)
         plt.clf()
         if (Output_Para.HEALpix_cart):
            hp.cartview(pix, fig = 1)           
         else:
            hp.mollview(pix, fig = 1)
         if (Output_Para.HEALpix_grat):
            hp.graticule()
         plt.show()
         plt.close()

         save_ques = Read_YN_Input("Do you want to save the plot (please enter Y, y, N, or n)? ")
         if save_ques :
           rc('text',usetex=True)
           plt.clf()
           if (Output_Para.HEALpix_cart):
              hp.cartview(pix, fig = 1)           
           else:
              hp.mollview(pix, fig = 1)
           if (Output_Para.HEALpix_grat):
              hp.graticule()
           if (Output_Para.log_scale):
              fname = 'Full_Sky_Surface_Brightness_Profile_log_%i_%i.pdf'%(nside,(k+1))
           else:
              fname = 'Full_Sky_Surface_Brightness_Profile_%i_%i.pdf'%(nside,(k+1))
           plt.title(r'Surface Brightness Profile at redshift between %0.3f and %0.3f'%(Halo_data[k].z_min,Halo_data[k].z_max),fontsize = 20)
           print 'Saving plot', fname
#         savefig(fdir+fname,bbox_inches='tight')
           plt.savefig(fdir+fname)
           rc('text',usetex=False)
           plt.close()

         save_ques = Read_YN_Input("Do you want to save the map data (please enter Y, y, N, or n)? ")
         if save_ques :
           if (Output_Para.log_scale):
              fname = 'Full_Sky_Surface_Brightness_Profile_log_HEALPix_map_%i_%i.txt'%(nside,(k+1))
           else:
              fname = 'Full_Sky_Surface_Brightness_Profile_HEALPix_map_%i_%i.txt'%(nside,(k+1))
           print 'Saving data', fname
           f = open(fdir+fname,'w')
           f.write("#   Pix_Value \n")
           savetxt(f, array([pix]).T)
           f.close()

