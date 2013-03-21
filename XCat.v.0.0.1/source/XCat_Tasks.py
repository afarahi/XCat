from XCat_Read_Catalog          import Read_Halo_Cat
from XCat_Cosmology_Parameters  import Input_Parameters
from XCat_Halos_Data            import Halo_Object
from XCat_Solver_Initial        import Solver
#from test                       import test

def main_tasks():
#    test()
    Halos_info = Read_Halo_Cat()
    Input_Param= Input_Parameters()
    Halo_data  = Halo_Object(Halos_info,Input_Param)
    Halo_data  = Solver(Halo_data)
#    Cosmo = Input_Parameters()
    return 0

'''
from matplotlib.pyplot      import *
from Solver_definition      import *
from Gravity_Power_Spectrum import Power_Spectrum_Plot_Construction
from Gravity_Parameters     import Gravity_obj
from Gravity_Utilities      import read_data_string
from Gravity_Report         import Creat_Report

def Gravity_Solver():
    #Solver Type
    Geometry_type_name = read_data_string(tag_name='Geometry_type',file_name='parameters/parameters.xml')
    Solver_type_name   = read_data_string(tag_name ='Solver_type',file_name ='parameters/parameters.xml')
    Solver_type        = Geometry_type_name + "+" + Solver_type_name
    if (Solver_type == "AdS4+RK4"):
       return AdS4_RK4_solver
    else:
       print "ERROR : THE SOLVER IS NOT DEFINED FOR THIS GEOMETRY + SOLVER TYPE"
       return NO_SOLVER


def main_tasks():

    Gravity_object = Gravity_obj()    
    Solver         = Gravity_Solver() 
    Solver(Gravity_object)

    if Gravity_object.field.Horizon :
       print "Horizon time is : ", Gravity_object.field.time
    else:
       print "Horizon is not formed ...! (You may want to increase i_max)"

    if Gravity_object.output.Power_Spectrum_status:
       Power_Spectrum_Plot_Construction(Gravity_obj,file_loc_save="Output/Power_Spectrum_data/",file_loc_load="Output/Power_Spectrum_data/")

    if Gravity_object.output.Report_status:
       Creat_Report(Gravity_object)

    #figure(1)
    #plot(Gravity_object.field.r,Gravity_object.field.Pi)
    #show()
    #figure(2)
    #plot(Gravity_object.field.r,Gravity_object.field.Phi)
    #show()

'''
