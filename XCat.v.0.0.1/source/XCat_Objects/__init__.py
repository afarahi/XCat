import warnings

try:
    ImportWarning
except NameError:
    class ImportWarning(Warning):
        pass

try:
    from XCat_Conversions_Constants   import *
except ImportError:
    warnings.warn("Warning: Cannot import visualisation tools (needs numpy)",
                  category=ImportWarning)

try:
    from XCat_Output_Parameters       import Output_Parameters
    from XCat_Input_Parameters        import Input_Parameters
    from XCat_Halos_Data              import Halo_Object
except ImportError:
    warnings.warn("Warning: Cannot import visualisation tools (needs numpy)",
                  category=ImportWarning)

