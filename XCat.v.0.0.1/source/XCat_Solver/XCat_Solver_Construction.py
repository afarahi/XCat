from XCat_Properties import Solver_menu

def Solver_Construction(Halo_data,Input_Param,General_Prop):

    while (True):
       ans = Solver_menu()
       if (ans == 1):
          from XCat_LxTx_Solver import LxTx_Solver
          LxTx_Solver(Halo_data,Input_Param)
          General_Prop.LxTx_Solved = True
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

#    return Halo_data
