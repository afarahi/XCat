from XCat_Utilities  import read_data_float

class Henry_et_al_2009_Parameters:

    def __init__(self):

       #Parameters
       self.alpha_T = read_data_float(tag_name = 'alpha_T',file_name = 'parameters/Models/Henry_et_al_2009_parameters.xml')
       self.T_15    = read_data_float(tag_name = 'T_15',file_name = 'parameters/Models/Henry_et_al_2009_parameters.xml')
       self.siglnT  = read_data_float(tag_name = 'sigma_ln_T',file_name = 'parameters/Models/Henry_et_al_2009_parameters.xml')

