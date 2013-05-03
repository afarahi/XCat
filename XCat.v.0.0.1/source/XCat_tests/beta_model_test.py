from XCat_Objects                  import ( Output_Parameters, Input_Parameters, Halo_Brightness_Surface_Sample_Object, 
                                            Halo_Object, Halo_General_Properties, pi, DtoR, RtoD)
from XCat_Utilities                import *
from XCat_Properties               import *
from XCat_LxTx_Solver              import *
from XCat_halo_separator           import *
from XCat_Output_Construction      import *
from XCat_Solver_Construction      import *
from XCat_Catalog_Manipulation     import *
from XCat_Separators_Construction  import *

from numpy                      import log, log10, exp, sqrt, zeros, savetxt, array, linspace
from matplotlib                 import rc
import matplotlib.pyplot          as plt
import healpy                     as hp


def beta_model_test():
  Print_logo()
  raw_input("Press enter to continue ... ")
  Input_Param  = Input_Parameters()
  Output_Param = Output_Parameters()
  General_Prop = Halo_General_Properties()
  #Reading data
  Halos_info   = Read_Halo_Cat_fit()
  Halo_data    = Halo_Object(Halos_info,Input_Param,General_Prop)
  del Halos_info
  #Separating into redshift peaces
  Halo_data.redshift_org(Input_Param)
  Halo_data    = red_shift_halo_separator(Halo_data,General_Prop)
  #Solving for Lx Tx
  LxTx_Solver(Halo_data,Input_Param)     
  #Creating brightness surface of a given halo and compaing it to theoretical beta model
  #
  #Creating bightness surface of given halo
  ques = True
  while(ques):
    nside = Output_Param.nside
    Sl_n  = len(Halo_data)
    k     = Read_Integer_Input("We have %i redshift slice  which one you want exctract the halo ? "%Sl_n)
    k     = int(k) - 1
    while(k > (Sl_n-1) or k < 0 ):
      print "Invalid Number."
      k = Read_Integer_Input("Please choose an integer between 1 and %i : "%Sl_n)
      k = int(k) - 1
    n   = len(Halo_data[k].RA[:])
    if (n == 0):
       print "There is no halo in this piece of redshift, please choos another one ..."
       raw_input("Press enter to continue ... ")
       return 

    halo_n = Read_Integer_Input("We have %i halos in this slice which one you want to exctract ? "%n)
    halo_n = halo_n - 1
    while(halo_n > (n-1) or halo_n < 0 ):
      print "Invalid Number."
      halo_n = Read_Integer_Input("Please choose an integer between 1 and %i : "%n)
      halo_n = int(halo_n) - 1

    Halo_Sample = Halo_Brightness_Surface_Sample_Object(Halo_data[k],Input_Param,Output_Param,halo_n)

    pix    = zeros(12*nside**2)
    for i in range(len(Halo_Sample.sRA[:])):
       j   = hp.ang2pix(nside,DtoR*(90.0-Halo_Sample.sDEC[i]),DtoR*(Halo_Sample.sRA[i]))
       pix[j] += Halo_Sample.sSB[i]
    pix    = pix/(12.0*nside**2)
    plt.clf()
    hp.gnomview(pix, fig=1 , rot=(Halo_Sample.RA,Halo_Sample.DEC,0.0) , xsize=Output_Param.xsize , reso=Output_Param.resolution , degree=Output_Param.resol_degree)
    hp.graticule()
    plt.show()
    plt.close()

    save_ques = Read_YN_Input("Do you want to save its picture (please enter Y, y, N, or n)? ")
    if save_ques :
       rc('font',family='serif')
       fdir  = './Output/plots/HEALPixSurfaceBrightness/'
       rc('text',usetex=True)
       plt.clf()
       hp.gnomview(pix , fig = 1 , rot = (Halo_Sample.RA,Halo_Sample.DEC,0.0) , xsize = Output_Param.xsize , reso = Output_Param.resolution, degree = Output_Param.resol_degree)
       hp.graticule()
       fname = 'test_mode_sky_projection_HEALPix_Surface_Brightness_Profile_%i_%i_%i.pdf'%(nside,(halo_n+1),(k+1))
       plt.title(r'Surface Brightness Profile (test mode)',fontsize = 20)
       print 'Saving plot', fname
       plt.savefig(fdir+fname)
       rc('text',usetex=False)
       plt.close()

    #Sample halo brightness surface is created 
    Rc    =  Halo_Sample.Rc
    beta  = Input_Param.SB_beta
    power = -3.0*beta+0.5
    #Calculating SB0
    #SB0   = max(pix) #(VERY SIMPLE AND NOT COMPLETELY RIGHT)
    '''
    # THIS ONE IS NOT WORKING 
    for ipix in range(len(pix)):
       if (pix[ipix] > 0.0):
         (theta,phi) = hp.pix2ang(nside,ipix)
         dtheta = theta - DtoR*(90.0-Halo_Sample.DEC)
         if(phi > pi):
           phi -= 2.0*pi
         dphi   = phi   - DtoR*Halo_Sample.RA
         rs     = sqrt(dtheta**2 + dphi**2)*Halo_Sample.d
         if (rs > 5.0*Rc):
            SB0 = pix[ipix] / (1. + (rs/Rc)**2)**power 
            break
    '''
    plt.clf()
    plt.figure(1)  
    num_SB0 = 0
    SB0     = 0.0

    #Realization of halo sample
    for ipix in range(len(pix)):
       if (pix[ipix] > 0.0):
         (theta,phi) = hp.pix2ang(nside,ipix)
         dtheta = theta - DtoR*(90.0-Halo_Sample.DEC)
         if(phi > pi):
           phi -= 2.0*pi
         dphi   = phi   - DtoR*Halo_Sample.RA
         rs     = sqrt(dtheta**2 + dphi**2)*Halo_Sample.d/Rc
         plt.semilogy(rs,pix[ipix],'r.')
         SB0 += pix[ipix] / (1. + rs**2)**power
         num_SB0 += 1
    SB0 = SB0/float(num_SB0)

    #Realization of beta model for this halo
    r     = linspace(0.0,12.0,101)
    SB    = zeros(len(r))

    for i in range(len(r)):
       #S(r) = S_0 * ( 1 + (r/Rc)^2 )^(-3*beta+0.5)
       SB[i] = SB0 * (1. +  r[i]**2 )**power
    plt.semilogy(r,SB,'b',label='Beta model')
    plt.xlim([min(r),max(r)])
    del SB0, beta, power, Rc, r, SB

    plt.title("Brightness surface (beta model)")
    plt.show()
    plt.close()

    del pix, rs
   
    ques = Read_YN_Input("Do you want to look at another halo? ")

  return 0

