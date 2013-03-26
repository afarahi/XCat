from XCat_Objects               import Input_Parameters, Output_Parameters, Halo_Object
from XCat_Solver                import LxTx_Solver
from XCat_Output_Construction   import *
from XCat_Catalog_Manipulation  import *

def main_tasks():
    Halos_info   = Read_Halo_Cat_fit()
    Input_Param  = Input_Parameters()
    Output_Param = Output_Parameters()
    Halo_data    = Halo_Object(Halos_info,Input_Param)
    Halo_data  = LxTx_Solver(Halo_data,Input_Param)
    Output_const(Halo_data,Input_Param,Output_Param)
    return 0

def test_tasks():
    from test   import test
    test()
    return 0
