import warnings

try:
    ImportWarning
except NameError:
    class ImportWarning(Warning):
        pass

try:
    from XCat_plot_sky_proj_healpy import (plot_sky_projection_healpy_count, 
                                           plot_sky_projection_healpy_simple,
                                           plot_sky_projection_healpy_all)  
except ImportError:
    warnings.warn("Warning: Cannot import visualisation tools (needs matplotlib and healpy)",
                  category=ImportWarning)

try:
    from XCat_plot_sky_proj        import plot_sky_projection
except ImportError:
    warnings.warn("Warning: Cannot import visualisation tools (needs matplotlib and healpy)",
                  category=ImportWarning)

try:
    from XCat_plot_TxLx            import plot_TxLx
except ImportError:
    warnings.warn("Warning: Cannot import visualisation tools (needs matplotlib and healpy)",
                  category=ImportWarning)
