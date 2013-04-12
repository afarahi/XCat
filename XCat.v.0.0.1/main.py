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
sys.path.insert(0,sys.path[11]+'/healpy')

from XCat_Tasks import main_tasks
from test       import test

main_tasks()
#test()
