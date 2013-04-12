from numpy        import matrix
from XCat_Objects import Z_Sliced_Halo_Object

def red_shift_halo_seperator(halo_data):
    seperated_halos_data = [] 
    for i in range(halo_data.Z_slice):
        seperated_halos_data.append(Z_Sliced_Halo_Object())
        seperated_halos_data[i].Creat_Halo_data(halo_data,i)
#       halo = halo_data
#       seperated_halos_data.append(halo)
#       seperated_halos_data[i].Redshift_Extract_Halo_data(i)
#       del halo
    raw_input("Press enter to continue ... ")

    return seperated_halos_data
