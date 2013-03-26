import warnings

try:
    ImportWarning
except NameError:
    class ImportWarning(Warning):
        pass

try:
    from XCat_Read_Catalog import Read_Halo_Cat_fit
except ImportError:
    warnings.warn("Warning: Cannot import visualisation tools (needs numpy)",
                  category=ImportWarning)

