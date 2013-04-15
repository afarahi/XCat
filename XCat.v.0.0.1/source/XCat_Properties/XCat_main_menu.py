import os
from XCat_Utilities import Read_Integer_Input

def Main_menu():
    os.system('clear')
    print " Main Menu : "
    print " (1)  Loading new input parameters. "
    print " (2)  Loading new output parameters. "
    print " (3)  Loading new halos catalog. "
    print " (4)  Adding new halos catalog. "
    print " (5)  Manipulating halos data. "
    print " (6)  Solvers. "
    print " (7)  Plotting. "
    print " (8)  Creating Report. "
    print " (9)  Changing Parameters manualy "
    print " (10) Exit. "
    print "-------------------------------------------------------"   
    ans = Read_Integer_Input(" Please enter a number : ")
    return ans

