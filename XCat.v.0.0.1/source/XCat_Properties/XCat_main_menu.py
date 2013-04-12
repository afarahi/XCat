import os
from XCat_Utilities import Read_Integer_Input

def Main_menu():
    os.system('clear')
    print " Main Menu : "
    print " (1)  For Loading new input parameters. "
    print " (2)  For Loading new output parameters. "
    print " (3)  For Loading new halos catalog. "
    print " (4)  For Adding new halos catalog. "
    print " (5)  For Dividing halos into redishift peaces. "
    print " (6)  For Solving Lx and Tx of halos. "
    print " (7)  For Plotting. "
    print " (8)  For Creating Report. "
    print " (9)  For Changing Parameters manualy "
    print " (10) Exit. "
    print "-------------------------------------------------------"   
    ans = Read_Integer_Input(" Please enter a number : ")
    return ans

