import warnings

try:
    ImportWarning
except NameError:
    class ImportWarning(Warning):
        pass

from XCat_LxTx_Solver import *

