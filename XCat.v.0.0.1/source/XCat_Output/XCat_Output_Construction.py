from XCat_plot   import *
from XCat_Report import *

def Output_const(Halo_data,Input_Parameters,Output_Parameters):

    if Output_Parameters.sky_projection :
       plot_sky_projection(Halo_data)
       print "Sky projection plot is created successfully."

    if Output_Parameters.HEALPix_sky_proj :
       plot_sky_projection_healpy_count(Halo_data,Output_Parameters.nside)
       print "Sky projection plot on HEALPix is created successfully."

    if Output_Parameters.Tx_Lx_plot :
       Output_Parameters.HEALpix_mod(Halo_data)
       print "(Tx,Lx) plot is created successfully."

    if Output_Parameters.Report:
       Creat_Report(Halo_data,Input_Parameters,Output_Parameters)
       print "Report is created successfully."


