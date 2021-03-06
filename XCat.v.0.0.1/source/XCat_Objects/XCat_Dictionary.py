from XCat_Lxm_module_Parameters import *
from XCat_Txm_module_Parameters import *
from XCat_plot                  import *

XCat_Dictionary = \
{
 "Lxm_module_parameters":
 {
   "Rozo_et_al_2012":Rozo_et_al_2012_Parameters ,
   "User":Lxm_user_Parameters ,
   "USER":Lxm_user_Parameters ,
   "user":Lxm_user_Parameters
 } ,
 "Txm_module_parameters":
 {
   "Henry_et_al_2009":Henry_et_al_2009_Parameters ,
   "User":Txm_user_Parameters ,
   "USER":Txm_user_Parameters ,
   "user":Txm_user_Parameters
 } ,
 "HEALPix_module":
 {
   "Count":plot_sky_projection_healpy_count ,
   "count":plot_sky_projection_healpy_count ,
   "Simple":plot_sky_projection_healpy_simple ,
   "simple":plot_sky_projection_healpy_simple ,
   "all":plot_sky_projection_healpy_all ,
   "All":plot_sky_projection_healpy_all
 }
} 


