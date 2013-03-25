from XCat_Input_Parameters      import Input_Parameters
from XCat_Read_Catalog          import Read_Halo_Cat_fit
from XCat_LxTx_Solver           import LxTx_Solver
from XCat_Halos_Data            import Halo_Object
from XCat_plot_sky_proj         import plot_sky_projection
from XCat_plot_TxLx             import plot_TxLx
def main_tasks():
    Halos_info = Read_Halo_Cat_fit()
    Input_Param= Input_Parameters()
    Halo_data  = Halo_Object(Halos_info,Input_Param)
    Halo_data  = LxTx_Solver(Halo_data,Input_Param)
    plot_TxLx(Halo_data)
#    plot_sky_projection(Halo_data)
    return 0

def test_tasks():
    from test   import test
    test()
    return 0

