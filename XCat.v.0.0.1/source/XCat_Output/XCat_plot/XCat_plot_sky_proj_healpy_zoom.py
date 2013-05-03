from XCat_Utilities              import Read_Integer_Input, Read_YN_Input 
from numpy                       import zeros, log10
from XCat_Objects                import DtoR
from matplotlib.pyplot           import *
from matplotlib                  import rc
import healpy                      as hp

def plot_sky_projection_healpy_count_zoom(Sliced_Halo_data,Output_Para):

    rc('font',family='serif')
    fdir  = './Output/plots/HEALPixZoom/'

    nside = Output_Para.nside

    Sl_n  = len(Sliced_Halo_data)
    Z_max = max(Sliced_Halo_data[Sl_n-1].Z_red[:])
    ques  = True

    while (ques):
      k = Read_Integer_Input("We have %i redshift slice  which one you want exctract the halo ? "%Sl_n)
      k = int(k) - 1
      while(k > (Sl_n-1) or k < 0 ):
        print "Invalid Number."
        k = Read_Integer_Input("Please choose an integer between 1 and %i : "%Sl_n)
        k = int(k) - 1

      pix     = zeros(12*nside**2)
      n       = len(Sliced_Halo_data[k].RA[:])
      if (n == 0):
         print "There is no halo in this piece of redshift, please choos another one ..."
         raw_input("Press enter to continue ... ")
         break 
         
      for i in range(n):
        j    = hp.ang2pix(nside,DtoR*(90.0-Sliced_Halo_data[k].DEC[i]),DtoR*(Sliced_Halo_data[k].RA[i]))
        pix[j] += 1
           
      halo_n = Read_Integer_Input("We have %i halos in this slice which one you want to exctract ? "%n)
      halo_n = halo_n - 1
      while(halo_n > (n-1) or halo_n < 0 ):
        print "Invalid Number."
        halo_n = Read_Integer_Input("Please choose an integer between 1 and %i : "%n)
        halo_n = halo_n - 1

# FOR TEST
#      j    = hp.ang2pix(nside,DtoR*(90.0-Sliced_Halo_data[k].DEC[halo_n]),DtoR*(Sliced_Halo_data[k].RA[halo_n]))
#      pix[j] += 1
 
      clf()
      hp.gnomview(pix, fig=1 , rot=(Sliced_Halo_data[k].RA[halo_n],Sliced_Halo_data[k].DEC[halo_n],0.0) , xsize=Output_Para.xsize , reso=Output_Para.resolution , degree=Output_Para.resol_degree)
      hp.graticule()
      show()

      save_ques = Read_YN_Input("Do you want to save its picture (please enter Y, y, N, or n)? ")
      if save_ques :
        rc('text',usetex=True)
        clf()
        hp.gnomview(pix, fig=1 , rot=(Sliced_Halo_data[k].RA[halo_n],Sliced_Halo_data[k].DEC[halo_n],0.0) , xsize=Output_Para.xsize , reso=Output_Para.resolution , degree=Output_Para.resol_degree)
        hp.graticule()
        fname = 'sky_projection_HEALPix_Count_%i_%i_%i.pdf'%(nside,(halo_n+1),(k+1))
        title(r'Redshift is between %0.2f and %0.2f'%(Sliced_Halo_data[k].z_min,Sliced_Halo_data[k].z_max),fontsize = 20)
        print 'Saving plot', fname
        savefig(fdir+fname,bbox_inches='tight')
        rc('text',usetex=False)
      ques = False
        
    return 0



def plot_sky_projection_healpy_simple_zoom(Sliced_Halo_data,Output_Para):
 
    rc('font',family='serif')
    fdir  = './Output/plots/HEALPixZoom/'
 
    nside = Output_Para.nside

    Sl_n  = len(Sliced_Halo_data)
    Z_max = max(Sliced_Halo_data[Sl_n-1].Z_red[:])
    ques  = True

    while (ques):
      k = Read_Integer_Input("We have %i redshift slice  which one you want exctract the halo ? "%Sl_n)
      k = int(k) - 1
      while(k > (Sl_n-1) or k < 0 ):
        print "Invalid Number."
        k = Read_Integer_Input("Please choose an integer between 1 and %i : "%Sl_n)
        k = int(k) - 1

      pix     = zeros(12*nside**2)
      n       = len(Sliced_Halo_data[k].RA[:])
      if (n == 0):
         print "There is no halo in this piece of redshift, please choos another one ..."
         raw_input("Press enter to continue ... ")
         break 

      for i in range(n):
        j    = hp.ang2pix(nside,DtoR*(90.0-Sliced_Halo_data[k].DEC[i]),DtoR*(Sliced_Halo_data[k].RA[i]))
        pix[j] += 10.0**Sliced_Halo_data[k].lgFx[i]
             
      halo_n = Read_Integer_Input("We have %i halos in this slice which one you want to exctract ? "%n)
      halo_n = halo_n - 1
      while(halo_n > (n-1) or halo_n < 0 ):
        print "Invalid Number."
        halo_n = Read_Integer_Input("Please choose an integer between 1 and %i : "%n)
        halo_n = halo_n - 1
 
      clf()
      hp.gnomview(pix, fig = 1 ,rot=(Sliced_Halo_data[k].RA[halo_n],Sliced_Halo_data[k].DEC[halo_n],0.0) , xsize=Output_Para.xsize , reso=Output_Para.resolution , degree=Output_Para.resol_degree)
      hp.graticule()
      show()
      close()

      save_ques = Read_YN_Input("Do you want to save its picture (please enter Y, y, N, or n)? ")
      if save_ques :
        rc('text',usetex=True)
        clf()
        hp.gnomview(pix, fig=1 , rot=(Sliced_Halo_data[k].RA[halo_n],Sliced_Halo_data[k].DEC[halo_n],0.0) , xsize=Output_Para.xsize , reso=Output_Para.resolution , degree=Output_Para.resol_degree)
        hp.graticule()
        fname = 'sky_projection_HEALPix_Simple_%i_%i_%i.pdf'%(nside,(halo_n+1),(k+1))
        title(r'Redshift is between %0.2f and %0.2f'%(Sliced_Halo_data[k].z_min,Sliced_Halo_data[k].z_max),fontsize = 20)
        print 'Saving plot', fname
#        savefig(fdir+fname,bbox_inches='tight')
        savefig(fdir+fname)
        rc('text',usetex=False)
        close()

      ques = False

    return 0


def plot_sky_projection_healpy_linear_zoom(Sliced_Halo_data,Output_Para):

    rc('font',family='serif')
    fdir  = './Output/plots/HEALPixZoom/'

    nside = Output_Para.nside

    Sl_n  = len(Sliced_Halo_data)
    Z_max = max(Sliced_Halo_data[Sl_n-1].Z_red[:])
    ques  = True

    while (ques):
      k = Read_Integer_Input("We have %i redshift slice  which one you want exctract the halo ? "%Sl_n)
      k = int(k) - 1
      while(k > (Sl_n-1) or k < 0 ):
        print "Invalid Number."
        k = Read_Integer_Input("Please choose an integer between 1 and %i : "%Sl_n)
        k = int(k) - 1

      pix     = zeros(12*nside**2)
      n       = len(Sliced_Halo_data[k].RA[:])
      if (n == 0):
         print "There is no halo in this piece of redshift, please choos another one ..."
         raw_input("Press enter to continue ... ")
         break 

      for i in range(n):
        j    = hp.ang2pix(nside,DtoR*(90.0-Sliced_Halo_data[k].DEC[i]),DtoR*(Sliced_Halo_data[k].RA[i]))
        neighbour = hp.get_all_neighbours(nside,j)
        Fx = 10.0**Sliced_Halo_data[k].lgFx[i] 
        pix[j]            += Fx/2.0
        pix[neighbour[0]] += Fx/16.0
        pix[neighbour[1]] += Fx/16.0
        pix[neighbour[2]] += Fx/16.0    
        pix[neighbour[3]] += Fx/16.0    
        pix[neighbour[4]] += Fx/16.0    
        pix[neighbour[5]] += Fx/16.0    
        pix[neighbour[6]] += Fx/16.0    
        pix[neighbour[7]] += Fx/16.0    

      halo_n = Read_Integer_Input("We have %i halos in this slice which one you want to exctract ? "%n)
      halo_n = halo_n - 1
      while(halo_n > (n-1) or halo_n < 0 ):
        print "Invalid Number."
        halo_n = Read_Integer_Input("Please choose an integer between 1 and %i : "%n)
        halo_n = halo_n - 1

# TEST
#      for i in range(halo_n,halo_n+1):
#        neighbour = hp.get_all_neighbours(nside,DtoR*(90.0-Sliced_Halo_data[k].DEC[i]),DtoR*(Sliced_Halo_data[k].RA[i]))
#       j    = hp.ang2pix(nside,DtoR*(90.0-Sliced_Halo_data[k].DEC[i]),DtoR*(Sliced_Halo_data[k].RA[i]))
#        pix[j] += 2.0
#        pix[neighbour[0]] += 1.0
#        pix[neighbour[1]] += 1.0    
#        pix[neighbour[2]] += 1.0   
#        pix[neighbour[3]] += 1.0
#        pix[neighbour[4]] += 1.0
#        pix[neighbour[5]] += 1.0
#        pix[neighbour[6]] += 1.0
#        pix[neighbour[7]] += 1.0
#        print j, neighbour
#        neighbour = hp.get_all_neighbours(nside,j)
#        print j, neighbour

      clf()
      hp.gnomview(pix, fig=1 , rot=(Sliced_Halo_data[k].RA[halo_n],Sliced_Halo_data[k].DEC[halo_n],0.0) , xsize=Output_Para.xsize , reso=Output_Para.resolution , degree=Output_Para.resol_degree)
      hp.graticule()
      show()
#      clf()
#      hp.mollview(pix, fig = 1)
#      hp.graticule()
#      show()
      close()
      save_ques = Read_YN_Input("Do you want to save its picture (please enter Y, y, N, or n)? ")
      if save_ques :
        rc('text',usetex=True)
        clf()
        hp.gnomview(pix, fig=1 , rot=(Sliced_Halo_data[k].RA[halo_n],Sliced_Halo_data[k].DEC[halo_n],0.0) , xsize=Output_Para.xsize , reso=Output_Para.resolution , degree=Output_Para.resol_degree)
        hp.graticule()
        fname = 'sky_projection_HEALPix_Linear_%i_%i_%i.pdf'%(nside,(halo_n+1),(k+1))
        title(r'Redshift is between %0.2f and %0.2f'%(Sliced_Halo_data[k].z_min,Sliced_Halo_data[k].z_max),fontsize = 20)
        print 'Saving plot', fname
#        savefig(fdir+fname,bbox_inches='tight')
        savefig(fdir+fname)
        rc('text',usetex=False)
        close()
      ques = False
#      ques = Read_YN_Input("Do you want to extract another halo (please enter Y, y, N, or n)? ")

    return 0



    
