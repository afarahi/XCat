import sys
sys.path.insert(0,sys.path[0]+'/source')
sys.path.insert(0,sys.path[0]+'/XCat_Objects')
sys.path.insert(0,sys.path[1]+'/XCat_Lxm_modules')
sys.path.insert(0,sys.path[2]+'/XCat_Txm_modules')
sys.path.insert(0,sys.path[3]+'/XCat_tests')
sys.path.insert(0,sys.path[4]+'/XCat_Calculator')
sys.path.insert(0,sys.path[5]+'/XCat_Utilities')
sys.path.insert(0,sys.path[6]+'/XCat_Output')
sys.path.insert(0,sys.path[7]+'/XCat_Output/XCat_plot')
sys.path.insert(0,sys.path[8]+'/XCat_Output/XCat_Report')
sys.path.insert(0,sys.path[9]+'/XCat_Solver')
sys.path.insert(0,sys.path[10]+'/XCat_Properties')
sys.path.insert(0,sys.path[11]+'/XCat_Seperators')
sys.path.insert(0,sys.path[12]+'/healpy')

from XCat_Tasks import main_tasks, test_tasks

print "(1) MAIN MODE"
print "(2) TEST MODE"

ans = int(raw_input("Please enter the mode number : "))
if (ans == 1):
    main_tasks()
if (ans == 2):
    test_tasks()
else:
    pass
