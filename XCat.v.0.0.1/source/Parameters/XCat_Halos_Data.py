#from XCat_Cosmology_Parameters import Input_Parameters
from numpy                     import log

class Halo_Object():

#   Cosmology = Input_Parameters()

   def __init__(self,Halos_info,Input_Param):

     self.X        = []
     self.Y        = []
     self.Z        = []

     self.RA       = []
     self.DEC      = []

     self.M500     = []
     self.R500     = []
     self.lgM500   = []

     self.Z_red    = []

     self.lgT      = []
     self.lnMT     = []
     self.lnML     = []
     self.lgLx     = []
     self.lgfx     = []
     self.lgLxobsf = []
     
     n = len(Halos_info.field('HALOPX')[:])

     for i in range(n):
       if(Halos_info.field('M500')[i] > Input_Param.Mlim):
          self.X.append(Halos_info.field('HALOPX')[i])
          self.Y.append(Halos_info.field('HALOPY')[i])
          self.Z.append(Halos_info.field('HALOPZ')[i])

          self.RA.append(Halos_info.field('RA')[i])
          self.DEC.append(Halos_info.field('DEC')[i])

          self.M500.append(Halos_info.field('M500')[i])
          self.R500.append(Halos_info.field('R500')[i])
          self.lgM500.append(log10(Halos_info.field('M500')[i])/(Input_Param.h_0 *1e14))

          self.Z_red.append(Halos_info.field('Z')[i])

          self.lgT.append(0.0)
          self.lnMT.append(0.0)
          self.lnML.append(0.0)
          self.lgLx.append(0.0)
          self.lgfx.append(0.0)
          self.lgLxobs.append(0.0)
     
     print "Number of Halos = ", n
     print "INITIALIZED SUCCESSFULLY."
      
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
