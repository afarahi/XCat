import warnings

try:
    ImportWarning
except NameError:
    class ImportWarning(Warning):
        pass

try:
    from XCat_plot_sky_proj_healpy import (plot_sky_projection_healpy_count , 
                                           plot_sky_projection_healpy_simple ,
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

try:
    from XCat_plot_logNlogS        import plot_logNlogS
except ImportError:
    warnings.warn("Warning: Cannot import visualisation tools (needs matplotlib and healpy)",
                  category=ImportWarning)

try:
   from XCat_plot_sky_proj_healpy_zoom import ( plot_sky_projection_healpy_count_zoom  ,
                                                plot_sky_projection_healpy_simple_zoom ,
                                                plot_sky_projection_healpy_linear_zoom )
except ImportError:
    warnings.warn("Warning: Cannot import visualisation tools (needs matplotlib and healpy)",
                  category=ImportWarning)

try:
   from XCat_plot_Halo_Surface_Brightness import plot_Halo_Surface_Brightness
except ImportError:
    warnings.warn("Warning: Cannot import visualisation tools (needs matplotlib and healpy)",
                  category=ImportWarning)
