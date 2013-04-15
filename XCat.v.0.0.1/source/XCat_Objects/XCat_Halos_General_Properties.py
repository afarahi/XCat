
class Halo_General_Properties():

   def __init__(self):

       self.total_sky_covered_deg2 = 0.0
       self.Z_redshift_max         = 0.0
       self.Hala_data_existence    = False
       self.LxTx_Solved            = False
       self.Redshift_peaces        = False
       self.Pix_separator          = False

   def update(self,Halo_data):

       DEC_max = max(Halo_data.DEC[:])
       DEC_min = min(Halo_data.DEC[:])
       RA_max  = max(Halo_data.RA[:])
       RA_min  = min(Halo_data.RA[:])
       
       self.total_sky_covered_deg2 = (DEC_max-DEC_min)*(RA_max-RA_min)
       self.Z_redshift_max         = max(Halo_data.Z_red[:])
       self.Hala_data_existence    = True
       self.LxTx_Solved            = False
       self.Redshift_peaces        = False
       self.Pix_separator          = False

   def Pix_separator_update(self,nside,pix_num):
       self.Pix_nside              = nside
       self.Pix_pixel_number       = pix_num
       
       


