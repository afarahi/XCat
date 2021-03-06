import warnings

try:
    ImportWarning
except NameError:
    class ImportWarning(Warning):
        pass

try:
    from XCat_Conversions_Constants    import *
except ImportError:
    warnings.warn("Warning: Cannot import ...",
                  category=ImportWarning)

try:
    from XCat_Output_Parameters        import Output_Parameters
    from XCat_Input_Parameters         import Input_Parameters
except ImportError:
    warnings.warn("Warning: Cannot import ...",
                  category=ImportWarning)

try:
    from XCat_Halos_Data               import ( Halo_Object, 
                                               Z_Sliced_Halo_Object )
except ImportError:
    warnings.warn("Warning: Cannot import XCat_Halos_Data",
                  category=ImportWarning)

try:
    from XCat_Halo_Brightness_Surface_Sample  import ( Halo_Brightness_Surface_Sample_Object )
except ImportError:
    warnings.warn("Warning: Cannot import XCat_Halos_Sample",
                  category=ImportWarning)

try:
    from XCat_Halos_General_Properties import Halo_General_Properties
except ImportError:
    warnings.warn("Warning: Cannot import XCat_Halos_Sample",
                  category=ImportWarning)

