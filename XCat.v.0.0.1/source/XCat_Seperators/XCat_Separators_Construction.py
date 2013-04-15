from XCat_Properties import Separators_menu

def Separators_Construction(Halo_data,Input_Param,General_Prop):

    Sliced_Halo_data = 0

    while (True):
       ans = Separators_menu()
       if (ans == 1):
           print " "
           from XCat_halo_separator import red_shift_halo_separator
           if (General_Prop.Hala_data_existence):
              Halo_data.redshift_org(Input_Param)
              Sliced_Halo_data = red_shift_halo_separator(Halo_data,General_Prop)
           else:
              print "Please add halo catalog ... "
              raw_input("Press enter to continue ... ")
       elif (ans == 2):
           from XCat_halo_separator import Pixel_separator
           if (General_Prop.Hala_data_existence):
              Halo_data = Pixel_separator(Halo_data,Input_Param,General_Prop)
           else:
              print "Please add halo catalog ... "
              raw_input("Press enter to continue ... ")
       elif (ans == 3):
           print "IT IS NOT IMPLIMENTED ... "
           raw_input("Press enter to continue ... ")
       elif (ans == 4):
           print "IT IS NOT IMPLIMENTED ... "
           raw_input("Press enter to continue ... ")
       elif (ans == 5):
           print "IT IS NOT IMPLIMENTED ... "
           raw_input("Press enter to continue ... ")
       elif (ans == 6):
           print "IT IS NOT IMPLIMENTED ... "
           raw_input("Press enter to continue ... ")
       elif (ans == 7):
           print "IT IS NOT IMPLIMENTED ... "
           raw_input("Press enter to continue ... ")
       elif (ans == 8):
           print "IT IS NOT IMPLIMENTED ... "
           raw_input("Press enter to continue ... ")
       elif (ans == 9):
           print "IT IS NOT IMPLIMENTED ..."
           raw_input("Press enter to continue ... ")
       elif (ans == 10):
           break

    return (Halo_data,Sliced_Halo_data)
