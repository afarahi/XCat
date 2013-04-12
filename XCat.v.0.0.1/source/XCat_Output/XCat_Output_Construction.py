from XCat_Objects    import Output_Parameters
from XCat_Utilities  import Read_YN_Input
from XCat_Properties import Plot_zoom_menu, Plot_menu
from XCat_plot       import *
from XCat_Report     import *

def Output_plot_zoom_mode(Halo_data,Input_Param,Output_Param):
    while (True):
       ans = Plot_zoom_menu()
       if (ans == 0):
          Output_Param  = Output_Parameters()
       elif (ans == 1):
          plot_sky_projection_healpy_count_zoom(Halo_data,Output_Param.nside)
       elif (ans == 2):
          plot_sky_projection_healpy_simple_zoom(Halo_data,Output_Param.nside)
       elif (ans == 3):
          plot_sky_projection_healpy_linear_zoom(Halo_data,Output_Param.nside)
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

def Output_plot(Halo_data,Input_Param,Output_Param):

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
          plot_TxLx(Halo_data)
          print "(Tx,Lx) plot is created successfully."
          raw_input("Press enter to continue ... ")
       elif (ans == 2):
          print " "
          plot_sky_projection_healpy_count(Halo_data,Output_Param.nside)
          print "Sky projection plot on HEALPix is created successfully."
          raw_input("Press enter to continue ... ")
       elif (ans == 3):
          Output_plot_zoom_mode(Halo_data,Input_Param,Output_Param)          
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
          print "IT IS NOT IMPLIMENTED ..."
       elif (ans == 10):
          break

def Output_report(Halo_data,Input_Param,Output_Param):
       Creat_Report(Halo_data,Input_Parameters,Output_Parameters)
       print "Report is created successfully."


