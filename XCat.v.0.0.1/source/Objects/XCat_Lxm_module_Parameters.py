from XCat_Utilities  import read_data_float

class Rozo_et_al_2012_Parameters():
  def __init__(self):
    #Parameters
    self.mass    = read_data_float(tag_name = 'mass',file_name = 'parameters/Models/Lxm/Rozo_et_al_2012_parameters.xml')
    self.a       = read_data_float(tag_name = 'a',file_name = 'parameters/Models/Lxm/Rozo_et_al_2012_parameters.xml')
    self.alpha   = read_data_float(tag_name = 'alpha',file_name = 'parameters/Models/Lxm/Rozo_et_al_2012_parameters.xml')
    self.LxExPow = read_data_float(tag_name = 'Lx_Ez_power',file_name = 'parameters/Models/Lxm/Rozo_et_al_2012_parameters.xml')
    self.siglnL  = read_data_float(tag_name = 'siglnL',file_name = 'parameters/Models/Lxm/Rozo_et_al_2012_parameters.xml')

class Lxm_user_Parameters():
  def __init__(self):
    #Parameters
    self.mass    = read_data_float(tag_name = 'mass',file_name = 'parameters/Models/Lxm/Lxm_user_parameters.xml')
    self.a       = read_data_float(tag_name = 'a',file_name = 'parameters/Models/Lxm/Lxm_user_parameters.xml')
    self.alpha   = read_data_float(tag_name = 'alpha',file_name = 'parameters/Models/Lxm/Lxm_user_parameters.xml')
    self.LxExPow = read_data_float(tag_name = 'Lx_Ez_power',file_name = 'parameters/Models/Lxm/Lxm_user_parameters.xml')
    self.siglnL  = read_data_float(tag_name = 'siglnL',file_name = 'parameters/Models/Lxm/Lxm_user_parameters.xml')

