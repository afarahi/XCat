import warnings

try:
    ImportWarning
except NameError:
    class ImportWarning(Warning):
        pass

try:
    from XCat_Conversions_Constants   import *
except ImportError:
    warnings.warn("Warning: Cannot import ...",
                  category=ImportWarning)

try:
    from XCat_Output_Parameters       import Output_Parameters
    from XCat_Input_Parameters        import Input_Parameters
except ImportError:
    warnings.warn("Warning: Cannot import ...",
                  category=ImportWarning)

try:
    from XCat_Halos_Data              import ( Halo_Object, 
                                               Z_Sliced_Halo_Object )
except ImportError:
    warnings.warn("Warning: Cannot import XCat_Halos_Data",
                  category=ImportWarning)

try:
    from XCat_Halos_Sample            import ( Halo_Sample_Object )
except ImportError:
    warnings.warn("Warning: Cannot import XCat_Halos_Sample",
                  category=ImportWarning)

try:
    from XCat_halo_seperator          import ( red_shift_halo_seperator )
except ImportError:
    warnings.warn("Warning: Cannot import ...",
                  category=ImportWarning)

