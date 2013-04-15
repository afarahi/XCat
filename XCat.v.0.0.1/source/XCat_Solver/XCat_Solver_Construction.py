from XCat_Properties import Solver_menu

def Solver_Construction(Halo_data,Input_Param,General_Prop):

    while (True):
       ans = Solver_menu()
       if (ans == 1):
          print " " 
          if (General_Prop.Redshift_peaces):
             from XCat_LxTx_Solver import LxTx_Solver
             Halo_data = LxTx_Solver(Halo_data,Input_Param)
             General_Prop.LxTx_Solved = True
          else:
             print "Please add halo catalog and/or divide halo into peaces ... "
          raw_input("Press enter to continue ... ")
       elif (ans == 2):
           print "IT IS NOT IMPLIMENTED ... "
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

    return Halo_data
