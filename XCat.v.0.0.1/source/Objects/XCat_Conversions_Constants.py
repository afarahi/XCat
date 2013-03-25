from XCat_Utilities  import read_data_float

pi = 3.141592653589793238462643383279502884197169
areasqdeg = pi*(180.0/pi)*(180.0/pi)

#! --- flux conversion: uses L in 1e44 erg/s
Gpc2cm = 3.086e27
fluxfac= ((1e22/Gpc2cm)*(1e22/Gpc2cm)/(4.0*pi))  #for cgs flux

###USELESS IDEA
'''
class Conversion_Constants:

    def __init__(self):

       #Flux_Conversion
       self.Flux_conv = read_data_float(tag_name = 'Gpc2cm',file_name = 'parameters/Conversion_Constants.xml')
       self.flux_fac  = (1e22/Gpc2cm)**2/(4.0*pi))

       #convert comoving distance to Gpc for assumed h0
       def Com_dis_to_Gpc(x,y,z,h0,z_red,ln_lobs):
           r2 = ( x**2 + y**2 + z**2 ) / ((1000*h0)**2)
           dlGpc2 = r2 * (1+z_red)**2
           fx = flux_fac * exp(ln_lobs) / dlGpc2
           return fx
'''
