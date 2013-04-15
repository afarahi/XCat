from XCat_Objects                  import ( Output_Parameters, Input_Parameters,
                                            Halo_Object, Halo_General_Properties)
from XCat_Utilities                import *
from XCat_Properties               import *
from XCat_Output_Construction      import *
from XCat_Solver_Construction      import *
from XCat_Catalog_Manipulation     import *
from XCat_Separators_Construction  import *

def main_tasks():

   Print_logo()
   raw_input("Press enter to continue ... ")
   Input_Param  = Input_Parameters()
   Output_Param = Output_Parameters()
   General_Prop = Halo_General_Properties()
   if Input_Param.Auto_mode :
          print "THIS IS NOT WORKING FOR NOW"
   else:
     Sliced_Halo_data = 0
     Halo_data        = 0
     while (True):
       ans = Main_menu()
       if (ans == 1):
          Input_Param  = Input_Parameters()
       elif (ans == 2):
          Output_Param = Output_Parameters()
       elif (ans == 3):
          Halos_info   = Read_Halo_Cat_fit()
          Halo_data    = Halo_Object(Halos_info,Input_Param,General_Prop)
          del Halos_info
       elif (ans == 4):
          file_name    = Read_String_Input("Please enter your file name (Note that your input file should be located at ./Catalog/Input_File/) : ")
          Halos_info   = Read_Halo_Cat_fit(file_name)
          if Halos_info:
             Halo_data.add_new_catalog(Halos_info,Input_Param,General_Prop)
          del Halos_info
       elif (ans == 5):
          (Halo_data,Sliced_Halo_data) = Separators_Construction(Halo_data,Input_Param,General_Prop)
       elif (ans == 6):
          Halo_data = Solver_Construction(Sliced_Halo_data,Input_Param,General_Prop)
       elif (ans == 7):
          if (General_Prop.Redshift_peaces):
             Output_plot(Sliced_Halo_data,Input_Param,Output_Param,General_Prop)
          else:
             print "Please add halo catalog and/or divide halo into peaces ... "
             raw_input("Press enter to continue ... ")
       elif (ans == 8):
           print "THIS PART IS NOT WORKING"
           raw_input("Press enter to continue ... ")
#             Output_report(Sliced_Halo_data,Input_Param,Output_Param)
       elif (ans == 9):
          print "IT IS NOT IMPLIMENTED ..."
       elif (ans == 10):
          print "Thank you for using XCat (V.0.0.1)"
          raw_input("Press enter to exit ... ")
          break
#    Halo_data     = LxTx_Solver(Halo_data,Input_Param)
#    Sliced_Halo_data = red_shift_halo_seperator(Halo_data)
#    del Halo_data
#    Output_const(Sliced_Halo_data,Input_Param,Output_Param)

#    from XCat_plot_sky_proj_healpy_zoom import *
#    plot_sky_projection_healpy_count_zoom(Sliced_Halo_data,Output_Param.nside)
   return 0

def test_tasks():
    from test   import test
    test()
    return 0
