from math         import sin, cos, tan, atan, asin
from XCat_Objects import pi, DtoR

def EquatorialTOGalactic(RA,DEC):
    # l
    gLong = 303.0*DtoR - atan( sin(192.25*DtoR-RA*DtoR) / (cos(192.25*DtoR-RA*DtoR)*sin(27.4*DtoR) - tan(DEC*DtoR)*cos(27.4*DtoR)) )
    # b
    gLati = asin(sin(DEC*DtoR)*sin(27.4*DtoR) + cos(DEC*DtoR)*cos(27.4*DtoR)*cos(192.25*DtoR-RA*DtoR))
    return (gLong/DtoR,gLati/DtoR)
