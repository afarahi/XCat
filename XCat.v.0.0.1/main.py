import sys
sys.path.insert(0,sys.path[0]+'/source')
sys.path.insert(0,sys.path[0]+'/Objects')
sys.path.insert(0,sys.path[1]+'/Lxm_modules')
sys.path.insert(0,sys.path[2]+'/Txm_modules')
sys.path.insert(0,sys.path[3]+'/tests')
sys.path.insert(0,sys.path[4]+'/Calculator')
sys.path.insert(0,sys.path[5]+'/Utilities')
sys.path.insert(0,sys.path[6]+'/Output')
sys.path.insert(0,sys.path[7]+'/Output/plot')


from XCat_Tasks import main_tasks
from test       import test

main_tasks()
#test()
