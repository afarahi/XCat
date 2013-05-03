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
    from XCat_plot_mass_function   import plot_mass_function
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
   from XCat_plot_file_mode            import ( load_map_file, 
                                                plot_zoom_sky,
                                                plot_full_sky_cart,
                                                plot_full_sky_normal )
except ImportError:
    warnings.warn("Warning: Cannot import visualisation tools (needs matplotlib and healpy)",
                  category=ImportWarning)


try:
   from XCat_plot_Halo_Surface_Brightness import (plot_Single_Halo_Surface_Brightness ,
                                                  plot_Pixel_Halos_Surface_Brightness ,
                                                  plot_Total_Sky_Halos_Surface_Brightness)
except ImportError:
    warnings.warn("Warning: Cannot import visualisation tools (needs matplotlib and healpy)",
                  category=ImportWarning)
