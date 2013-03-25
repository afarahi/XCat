from XCat_Utilities  import read_data_string, read_data_float, read_data_int, read_data_bool 

class Output_Parameters:

   def __init__(self):

      #PLots         
      self.sky_projection  = read_data_bool(tag_name = 'sky_projection',file_name = 'parameters/Output.xml')

      #Report
      self.Report  = read_data_bool(tag_name = 'Report',file_name = 'parameters/Output.xml')
      

