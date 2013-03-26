from numpy import sqrt

# Evolutionary Factor
def Evolution_factors(Cosmology,zred):
    Ez   = sqrt(Cosmology.Omega_M*(1+zred)**3 + Cosmology.Omega_DE)
    EzRo = sqrt(Cosmology.Omega_M*(1+0.23)**3 + Cosmology.Omega_DE)
    return (Ez,EzRo)
