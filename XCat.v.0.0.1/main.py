import sys
sys.path.insert(0,sys.path[0]+'/source')
sys.path.insert(0,sys.path[0]+'/Parameters')
sys.path.insert(0,sys.path[1]+'/Solver')
sys.path.insert(0,sys.path[2]+'/Tx_module')
sys.path.insert(0,sys.path[3]+'/tests')
sys.path.insert(0,sys.path[4]+'/Calculator')

from XCat_Tasks import main_tasks
from test       import test

#main_tasks()
test()
