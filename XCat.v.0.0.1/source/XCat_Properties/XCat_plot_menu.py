import os
from XCat_Utilities import Read_Integer_Input

def Plot_menu():
    os.system('clear')
    print " Plot Menu : "
    print " (0)  Change ouput parameters localy. "
    print " (1)  (Tx,Lx) plot. "
    print " (2)  Sky projection plot on HEALPix (Total sky mode). "
    print " (3)  Sky projection plot on HEALPix (Zoom mode). "
    print " (4)  Surface Brightness of a halo. "
    print " (5)  (logN,logS) plot "
    print " (6)  Mass function "
    print " (7)  For ... "
    print " (8)  For ... "
    print " (9)  Plot map of given file in HEALPix. "
    print " (10) Back to main menu. "
    print "-------------------------------------------------------"   
    ans = Read_Integer_Input(" Please enter a number : ")
    print "  "
    return ans

def Plot_zoom_menu():
    os.system('clear')
    print " Plotting Menu : "
    print " (0)  Change ouput parameters localy. "
    print " (1)  Zoom count mode. "
    print " (2)  Zoom flux (simple) mode. "
    print " (3)  Zoom flux (linear) mode. "
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

def Plot_surface_brightness_menu():
    os.system('clear')
    print " Surface Brightness Menu : "
    print " (1)  Surface Brightness of a given halo.  "
    print " (2)  Surface Brightness of a given pixel.  "
    print " (3)  Surface Brightness of total sky. "
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

def Plot_surface_brightness_menu():
    os.system('clear')
    print " Surface Brightness Menu : "
    print " (1)  Surface Brightness of a given halo.  "
    print " (2)  Surface Brightness of a given pixel.  "
    print " (3)  Surface Brightness of total sky. "
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


def Plot_file_mode_menu():
    os.system('clear')
    print " Mapping sky : "
    print " (0)  Load a map file.  "
    print " (1)  Full Sky (Normal).  "
    print " (2)  Full Sky (Cartesian).  "
    print " (3)  Zoom mode. "
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

