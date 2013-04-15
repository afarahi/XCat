import os
from XCat_Utilities import Read_Integer_Input

def Solver_menu():
    os.system('clear')
    print " Solver Menu : "
    print " (1)  Solving Lx and Tx of halos. "
    print " (2)  For ... "
    print " (3)  For ... "
    print " (4)  For ... "
    print " (5)  For ... "
    print " (6)  For ... "
    print " (7)  For ... "
    print " (8)  For ... "
    print " (9)  For ... "
    print " (10) Back to main menu. "
    print "-------------------------------------------------------"   
    ans = Read_Integer_Input(" Please enter a number : ")
    print "  "
    return ans
