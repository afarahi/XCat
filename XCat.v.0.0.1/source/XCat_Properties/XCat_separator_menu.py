import os
from XCat_Utilities import Read_Integer_Input

def Separators_menu():
    os.system('clear')
    print " Plot Menu : "
    print " (1)  Dividing halos into redishift peaces. "
    print " (2)  Extracting 1 HEALPix data for a given angular area of sky. "
    print " (3)  For ... "
    print " (4)  For ... "
    print " (5)  For ... "
    print " (6)  For ... "
    print " (7)  For ... "
    print " (8)  For ... "
    print " (9)  For ... "
    print " (10) Back to plotting menu. "
    print "-------------------------------------------------------"   
    ans = Read_Integer_Input(" Please enter a number : ")
    print "  "
    return ans

