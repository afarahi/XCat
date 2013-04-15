from XCat_Utilities  import read_data_string, read_data_float, read_data_int, read_data_bool 
from XCat_Dictionary import XCat_Dictionary

class Input_Parameters:

   def __init__(self):

      #Auto_mode
      self.Auto_mode   = read_data_bool(tag_name = 'Auto_mode',file_name = 'parameters/Input_Parameters.xml')

      #Cosmology         
      self.h_0         = read_data_float(tag_name = 'Hubble_Parameter',file_name = 'parameters/Cosmological_Parameters.xml')
      self.Omega_DE    = read_data_float(tag_name = 'Omega_DE',file_name = 'parameters/Cosmological_Parameters.xml')
      self.Omega_M     = read_data_float(tag_name = 'Omega_M',file_name = 'parameters/Cosmological_Parameters.xml')
      self.Omega_b     = read_data_float(tag_name = 'Omega_b',file_name = 'parameters/Cosmological_Parameters.xml')
      self.Omega_R     = read_data_float(tag_name = 'Omega_R',file_name = 'parameters/Cosmological_Parameters.xml')
      self.Omega_k     = read_data_float(tag_name = 'Omega_k',file_name = 'parameters/Cosmological_Parameters.xml')
      self.sigma_8     = read_data_float(tag_name = 'sigma_8',file_name = 'parameters/Cosmological_Parameters.xml')
      self.w           = read_data_float(tag_name = 'w',file_name = 'parameters/Cosmological_Parameters.xml')
      self.ns          = read_data_float(tag_name = 'ns',file_name = 'parameters/Cosmological_Parameters.xml')

      #Features
      self.red_shift_n = read_data_int(tag_name = 'red_shift_slices',file_name = 'parameters/Input_Parameters.xml')
      self.sample_num  = read_data_int(tag_name = 'Sample_Number',file_name = 'parameters/Input_Parameters.xml')
      self.SkySqrDeg   = read_data_float(tag_name = 'Squar_Degree',file_name = 'parameters/Input_Parameters.xml')

      #Models
      self.Lxm_mod     = read_data_string(tag_name = 'Lxm_model',file_name = 'parameters/Input_Parameters.xml')
      self.Txm_mod     = read_data_string(tag_name = 'Txm_model',file_name = 'parameters/Input_Parameters.xml')
      try:
         self.Lxm_para_obj= XCat_Dictionary["Lxm_module_parameters"][self.Lxm_mod]
      except KeyError:
         print "Input Lxm Parameter method is not matching with data ..."
         print "Please change your file and try again ..."
         raw_input("Press enter to continue ... ")
         pass
      try:
         self.Txm_para_obj= XCat_Dictionary["Txm_module_parameters"][self.Txm_mod]
      except KeyError:
         print "Input Txm Parameter method is not matching with data ..."
         print "Please change your file and try again ..."
         raw_input("Press enter to continue ... ")
         pass
      self.SB_beta        = read_data_float(tag_name = 'SB_beta',file_name = 'parameters/Input_Parameters.xml')
  
      #Exctra Parameters
      self.rTL         = read_data_float(tag_name = 'rTL_correlation',file_name = 'parameters/Input_Parameters.xml')

      #Limits
      self.Flim        = read_data_float(tag_name = 'F_limit',file_name = 'parameters/Input_Parameters.xml')
      self.Mlim        = read_data_float(tag_name = 'Mass_limit',file_name = 'parameters/Input_Parameters.xml')

      #Corrections
      self.K_corr      = read_data_float(tag_name = 'K_correction',file_name = 'parameters/Correction_Parameters.xml')
      K1 = read_data_float(tag_name = 'K1fac_1',file_name = 'parameters/Correction_Parameters.xml')
      K2 = read_data_float(tag_name = 'K1fac_2',file_name = 'parameters/Correction_Parameters.xml')
      K3 = read_data_float(tag_name = 'K1fac_3',file_name = 'parameters/Correction_Parameters.xml')
      self.K1fac       = [K1 , K2 , K3]
      K1 = read_data_float(tag_name = 'K2fac_1',file_name = 'parameters/Correction_Parameters.xml')
      K2 = read_data_float(tag_name = 'K2fac_2',file_name = 'parameters/Correction_Parameters.xml')
      K3 = read_data_float(tag_name = 'K2fac_3',file_name = 'parameters/Correction_Parameters.xml')
      self.K2fac       = [K1 , K2 , K3]
      
      print "COSMOLOGY and INPUTS are assigned SUCCESSFULLY."
