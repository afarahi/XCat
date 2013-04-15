from XCat_Utilities  import read_data_string, read_data_float, read_data_int, read_data_bool 
from XCat_Dictionary import XCat_Dictionary

class Output_Parameters:

   def __init__(self):

      #PLots         
      self.HEALPix_sky_proj= read_data_bool(tag_name = 'HEALPix_sky_projection',file_name = 'parameters/Output_Parameters.xml')
      self.sky_projection  = read_data_bool(tag_name = 'sky_projection',file_name = 'parameters/Output_Parameters.xml')
      self.Tx_Lx_plot      = read_data_bool(tag_name = 'Tx_Lx',file_name = 'parameters/Output_Parameters.xml')
      
      #HealPix Properties
      self.xsize        = read_data_int(tag_name = 'xsize',file_name = 'parameters/Output_Parameters.xml')
      self.nside        = read_data_int(tag_name = 'nside',file_name = 'parameters/Output_Parameters.xml')
      mod               = read_data_string(tag_name = 'HEALPix_module',file_name = 'parameters/Output_Parameters.xml')
      self.HEALpix_mod  = XCat_Dictionary["HEALPix_module"][mod]

      #Report
      self.Report  = read_data_bool(tag_name = 'Report',file_name = 'parameters/Output_Parameters.xml')


