from numpy        import matrix
from XCat_Objects import Z_Sliced_Halo_Object

def red_shift_halo_separator(Halo_data,General_Prop):
    separated_halos_data = [] 
    if (General_Prop.Hala_data_existence):
       for i in range(Halo_data.Z_slice):
          separated_halos_data.append(Z_Sliced_Halo_Object())
          separated_halos_data[i].Creat_Halo_data(Halo_data,i)
       General_Prop.Redshift_peaces = True
    else:
       "First you need to add a halo catalog ..."
    raw_input("Press enter to continue ... ")
    return separated_halos_data


def Pixel_separator(Halo_data,Input_Para,General_Prop):
    import healpy as hp
    from XCat_Objects import DtoR, Halo_Object
    from XCat_Utilities import Read_Integer_Input

    nside = 1
    while ( Input_Para.SkySqrDeg < 64800.0/float(hp.nside2npix(2*nside)) ):
         nside = 2*nside

    if (General_Prop.Hala_data_existence):
       n = Halo_data.number_of_halos

       kp= Read_Integer_Input("We have %i halos in this slice which one you want to exctract ? "%n)
       kp= kp - 1
       while(kp > (n-1) or kp < 0 ):
          print "Invalid Number."
          kp= Read_Integer_Input("Please choose an integer between 1 and %i : "%n)
          kp= kp - 1
       k = hp.ang2pix(nside,DtoR*(90.0-Halo_data.DEC[kp]),DtoR*(Halo_data.RA[kp]))
       Pix_Halo_data = Halo_Object()
       for i in range(n):
           if ( k == hp.ang2pix(nside,DtoR*(90.0-Halo_data.DEC[i]),DtoR*(Halo_data.RA[i])) ):
              Pix_Halo_data.add_single_data(Halo_data,i)
       Pix_Halo_data.update_halo_data   
       General_Prop.update
       General_Prop.Pix_separator = True
       General_Prop.Pix_separator_update(nside,k)
    else:
       "First you need to add a halo catalog ..."
       Pix_Halo_data = None
    raw_input("Press enter to continue ... ")
    return Pix_Halo_data
