import warnings

try:
    ImportWarning
except NameError:
    class ImportWarning(Warning):
        pass

from XCat_logo            import Print_logo

from XCat_main_menu       import Main_menu

from XCat_plot_menu       import (Plot_menu,
                                  Plot_zoom_menu)  

from XCat_solver_menu     import Solver_menu

from XCat_separator_menu  import Separators_menu
