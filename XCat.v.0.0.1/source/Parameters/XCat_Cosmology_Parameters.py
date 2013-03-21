from XCat_Utilities  import read_data_string, read_data_float, read_data_int, read_data_bool 
from XCat_Dictionary import XCat_Dictionary

class Input_Parameters:

   def __init__(self):

      #Cosmology         
      self.h_0         = read_data_float(tag_name = 'Hubble_Parameter',file_name = 'parameters/Cosmological_Parameters.xml')
      self.Omega_DE    = read_data_float(tag_name = 'Omega_DE',file_name = 'parameters/Cosmological_Parameters.xml')
      self.Omega_M     = read_data_float(tag_name = 'Omega_M',file_name = 'parameters/Cosmological_Parameters.xml')
      self.Omega_b     = read_data_float(tag_name = 'Omega_b',file_name = 'parameters/Cosmological_Parameters.xml')
      self.Omega_R     = read_data_float(tag_name = 'Omega_R',file_name = 'parameters/Cosmological_Parameters.xml')
      self.Omega_k     = read_data_float(tag_name = 'Omega_k',file_name = 'parameters/Cosmological_Parameters.xml')
      self.sigma_8     = read_data_float(tag_name = 'sigma_8',file_name = 'parameters/Cosmological_Parameters.xml')

      #Models
      self.Basic_mod   = read_data_string(tag_name = 'Basic_parameters',file_name = 'parameters/Cosmological_Parameters.xml')
      self.Tx_conv_mod = read_data_string(tag_name = 'Tx_conversion_parameters',file_name = 'parameters/Cosmological_Parameters.xml')
      self.Solver      = XCat_Dictionary["Solver"][self.Basic_mod][0]
      self.Tx_module   = XCat_Dictionary["Tx_module"][self.Tx_conv_mod][0]

      #Exctra Parameters
      self.rTL         = read_data_float(tag_name = 'rTL_correlation',file_name = 'parameters/Cosmological_Parameters.xml')

      #Limits
      self.Flim        = read_data_float(tag_name = 'F_limit',file_name = 'parameters/Cosmological_Parameters.xml')
      self.Mlim        = read_data_float(tag_name = 'Mass_limit',file_name = 'parameters/Cosmological_Parameters.xml')

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
      
      print "COSMOLOGY IS SET SUCCESSFULLY."
      
'''
         self.Report_status         = read_data_bool(tag_name = 'Report_Status',file_name = 'parameters/output.xml')
         self.Power_Spectrum_status = read_data_bool(tag_name = 'Power_Spectrum_Status',file_name = 'parameters/output.xml')

         self.Frame_time_step       = read_data_int(tag_name = 'n_frame',file_name = 'parameters/output.xml')
         self.Number_of_data_points = read_data_int(tag_name = 'n_data_size',file_name = 'parameters/output.xml')
        
         #Output
         self.Pi_Field              = read_data_bool(tag_name = 'Pi_Field',file_name = 'parameters/output.xml')
         self.Pi_Field_max          = read_data_float(tag_name = 'Pi_Field_max',file_name = 'parameters/output.xml')
         self.Phi_Field             = read_data_bool(tag_name = 'Phi_Field',file_name = 'parameters/output.xml')
         self.Phi_Field_max         = read_data_float(tag_name = 'Phi_Field_max',file_name = 'parameters/output.xml')
         self.phi_Field             = read_data_bool(tag_name = 'phi_Field',file_name = 'parameters/output.xml')
         self.phi_Field_max         = read_data_float(tag_name = 'phi_Field_max',file_name = 'parameters/output.xml')
         self.Frame_format          = read_data_string(tag_name = 'Frame_format',file_name = 'parameters/output.xml')
         self.Data_file_name        = read_data_string(tag_name = 'Data_file_name',file_name = 'parameters/output.xml')
         
         #Power Spectrum
         self.Power_Spectrum_points = read_data_int(tag_name = 'Power_Spectrum_data_size',file_name = 'parameters/output.xml')
         self.Power_Spectrum_file_name = read_data_string(tag_name = 'Power_Spectrum_file_name',file_name = 'parameters/output.xml')
         self.Power_Spectrum_Setting_number = read_data_int(tag_name = 'Power_Spectrum_setting_number',file_name = 'parameters/output.xml')



         self.r            = []
         self.phi          = []
         self.Phi          = []
         self.Pi           = []
         self.Ricci_Scalar = []

         self.time         = 0.0
      
         self.Horizon      = False
         self.Horizon_r    = []
         
         self.Power_Spec_n = []
'''
