from XCat_Objects    import Output_Parameters
from XCat_Utilities  import Read_YN_Input
from XCat_Properties import Plot_surface_brightness_menu, Plot_file_mode_menu, Plot_zoom_menu, Plot_menu
from XCat_plot       import *
from XCat_Report     import *

def Output_plot(Halo_data,Input_Param,Output_Param,General_Prop):

#    if Output_Parameters.sky_projection :
#       plot_sky_projection(Halo_data)
#       print "Sky projection plot is created successfully."
    while (True):
       ans = Plot_menu()
       if (ans == 0):
           print " "
           Output_Param  = Output_Parameters()
       elif (ans == 1):
           print " "
           if (General_Prop.LxTx_Solved):
	       plot_TxLx(Halo_data)
               print "(Lx,Tx) plot is created successfully."
           else: 
               print "Please first solve for Lx-Tx ..."
           raw_input("Press enter to continue ... ")
       elif (ans == 2):
           print " "
           plot_sky_projection_healpy_count(Halo_data,Output_Param.nside)
           plot_sky_projection_healpy_simple(Halo_data,Output_Param.nside)
           print "Sky projection plot on HEALPix is created successfully."
           raw_input("Press enter to continue ... ")
       elif (ans == 3):
           Output_plot_zoom_mode(Halo_data,Input_Param,Output_Param,General_Prop)          
       elif (ans == 4):
           Output_plot_surface_brightness_mode(Halo_data,Input_Param,Output_Param,General_Prop)
       elif (ans == 5):
           if (General_Prop.LxTx_Solved):
              plot_logNlogS(Halo_data,Input_Param,Output_Param,General_Prop)
           else:
              print "Please first Solve for Lx-Tx ..."
              raw_input("Press enter to continue ... ")
       elif (ans == 6):
           plot_mass_function(Halo_data,Input_Param,Output_Param,General_Prop)           
       elif (ans == 7):
           print "IT IS NOT IMPLIMENTED ... "
       elif (ans == 8):
           print "IT IS NOT IMPLIMENTED ... "
       elif (ans == 9):
           Output_plot_file_mode(Output_Param)
       elif (ans == 10):
           break


def Output_plot_zoom_mode(Halo_data,Input_Param,Output_Param,General_Prop):
    while (True):
       ans = Plot_zoom_menu()
       if (ans == 0):
           Output_Param  = Output_Parameters()
       elif (ans == 1):
           plot_sky_projection_healpy_count_zoom(Halo_data,Output_Param)
       elif (ans == 2):
           if (General_Prop.LxTx_Solved):
              plot_sky_projection_healpy_simple_zoom(Halo_data,Output_Param)
           else:
              print "Please first Solve for Lx-Tx ..."
              raw_input("Press enter to continue ... ")
       elif (ans == 3):
           if (General_Prop.LxTx_Solved):
              plot_sky_projection_healpy_linear_zoom(Halo_data,Output_Param)
           else:
              print "Please first Solve for Lx-Tx ..."
              raw_input("Press enter to continue ... ")
       elif (ans == 4):
           print "IT IS NOT IMPLIMENTED ... "
       elif (ans == 5):
           print "IT IS NOT IMPLIMENTED ... "
       elif (ans == 6):
           print "IT IS NOT IMPLIMENTED ... "
       elif (ans == 7):
           print "IT IS NOT IMPLIMENTED ... "
       elif (ans == 8):
           print "IT IS NOT IMPLIMENTED ... "
       elif (ans == 9):
           print "IT IS NOT IMPLIMENTED ... "
       elif (ans == 10):
           break

def Output_plot_surface_brightness_mode(Halo_data,Input_Param,Output_Param,General_Prop):
    while (True):
       ans = Plot_surface_brightness_menu()
       if   (ans == 1):
           if (General_Prop.LxTx_Solved):
              plot_Single_Halo_Surface_Brightness(Halo_data,Input_Param,Output_Param)
           else:
              print "Please first Solve for LxTx ..."
              raw_input("Press enter to continue ... ")
       elif (ans == 2):
           if (General_Prop.LxTx_Solved):
              plot_Pixel_Halos_Surface_Brightness(Halo_data,Input_Param,Output_Param)
           else:
              print "Please first Solve for LxTx ..."
              raw_input("Press enter to continue ... ")
       elif (ans == 3):
           if (General_Prop.LxTx_Solved):
              plot_Total_Sky_Halos_Surface_Brightness(Halo_data,Input_Param,Output_Param)
           else:
              print "Please first Solve for LxTx ..."
              raw_input("Press enter to continue ... ")
       elif (ans == 4):
           print "IT IS NOT IMPLIMENTED ... "
       elif (ans == 5):
           print "IT IS NOT IMPLIMENTED ... "
       elif (ans == 6):
           print "IT IS NOT IMPLIMENTED ... "
       elif (ans == 7):
           print "IT IS NOT IMPLIMENTED ... "
       elif (ans == 8):
           print "IT IS NOT IMPLIMENTED ... "
       elif (ans == 9):
           print "IT IS NOT IMPLIMENTED ... "
       elif (ans == 10):
           break

def Output_plot_file_mode(Output_Param):
    npix = 0
    npix_bool = False
    while (True):
       ans = Plot_file_mode_menu()
       if   (ans == 0):
           (npix_bool,npix) = load_map_file()
       elif (ans == 1):
           plot_full_sky_normal(Output_Param,npix,npix_bool)
       elif (ans == 2):
           plot_full_sky_cart(Output_Param,npix,npix_bool)
       elif (ans == 3):
           plot_zoom_sky(Output_Param,npix,npix_bool)
       elif (ans == 4):
           print "IT IS NOT IMPLIMENTED ... "
       elif (ans == 5):
           print "IT IS NOT IMPLIMENTED ... "
       elif (ans == 6):
           print "IT IS NOT IMPLIMENTED ... "
       elif (ans == 7):
           print "IT IS NOT IMPLIMENTED ... "
       elif (ans == 8):
           print "IT IS NOT IMPLIMENTED ... "
       elif (ans == 9):
           print "IT IS NOT IMPLIMENTED ... "
       elif (ans == 10):
           del npix, npix_bool
           break


def Output_report(Halo_data,Input_Param,Output_Param):
    Creat_Report(Halo_data,Input_Parameters,Output_Parameters)
    print "Report is created successfully."


