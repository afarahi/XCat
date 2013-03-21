from numpy import exp
from XCat_Conversions_Constants  import fluxfac

def flux_cal(x,y,z,z_redshift,h_0,lnlobs): 
   #! --- convert comoving distance to Gpc for assumed h0
   r2     = ( x**2 + y**2 + z**2 ) / (1000.0*h_0)**2
   dlGpc2 = r2 * (1.0+z_redshift)**2
   fx = fluxfac * exp(lnlobs) / dlGpc2
   return fx
