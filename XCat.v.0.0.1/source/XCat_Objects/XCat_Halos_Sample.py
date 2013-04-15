from numpy        import zeros, sqrt
from random       import gauss, uniform
from XCat_Objects import DtoR, RtoD

class Halo_Sample_Object():

   def __init__(self,Halo_data,Input_Para,sample_code):

    sample_num = Input_Para.sample_num
    beta       = Input_Para.SB_beta

    self.sSB  = zeros(sample_num)
    self.sRA  = zeros(sample_num)
    self.sDEC = zeros(sample_num)

    self.DEC  = Halo_data.DEC[sample_code]
    self.RA   = Halo_data.RA[sample_code]
    self.R200 = Halo_data.R200[sample_code]
    self.r    = sqrt(Halo_data.X[sample_code]**2 + Halo_data.Y[sample_code]**2 + Halo_data.Z[sample_code]**2)

    self.SB0  = 1.0
 
    sigma = RtoD*self.R200/self.r
    i     = 0
    while (i < sample_num):
#       sRA[i] = gauss(self.RA,sigma)
#       sDEC[i]= gauss(self.DEC,sigma)
       self.sRA[i] = self.RA  + uniform(-sigma,sigma)
       self.sDEC[i]= self.DEC + uniform(-sigma,sigma)      
       sR     = self.r*(DtoR*sqrt((self.sRA[i]-self.RA)**2 + (self.sDEC[i]-self.DEC)**2))
       if (sR < self.R200):
         self.sSB[i] = self.SB0*(1.0 + (sR/self.R200)**2)**(-3.0*beta+0.5)/sample_num
         i += 1

   def add_sample_data(self,RA,DEC,Fx,Z_red):
     self.RA       = RA
     self.DEC      = DEC
     self.Fx       = Fx

     self.Z_red    = Z_red
 
     self.Sample_nu= len(Fx[:])

