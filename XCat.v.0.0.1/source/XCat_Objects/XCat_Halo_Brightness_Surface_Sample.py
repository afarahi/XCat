from numpy        import zeros, sqrt
from random       import gauss, uniform
from XCat_Objects import DtoR, RtoD

def sample_num_calc(samp_coeff,nside,d,Rc):
    SN = 2.0e6*12.0*float(nside)*(Rc/d)**2
    print "Sample number : ", int(samp_coeff*SN)
    if (SN < 20.0):
        SN = 20.0
    return int(samp_coeff*SN)

class Halo_Brightness_Surface_Sample_Object():

   def __init__(self,Halo_data,Input_Para,Output_Para,sample_code):

    beta     = Input_Para.SB_beta

    self.DEC = Halo_data.DEC[sample_code]
    self.RA  = Halo_data.RA[sample_code]
    # Rc = R200 * 0.075 * (M200/10^12)^0.6
    # prescrition astro-ph/9703027
    # self.Rc   = Halo_data.R200[sample_code] * 0.075 * (Halo_data.M200[sample_code]/10**12)**0.6
    self.Rc  = 0.15*Halo_data.R200[sample_code]
    self.d   = sqrt(Halo_data.X[sample_code]**2 + Halo_data.Y[sample_code]**2 + Halo_data.Z[sample_code]**2)

    sample_num= sample_num_calc(Input_Para.samp_num_co,Output_Para.nside,self.d,self.Rc)

#    self.sSB = zeros(sample_num)
#    self.sRA = zeros(sample_num)
#    self.sDEC= zeros(sample_num)
    self.sSB = []
    self.sRA = []
    self.sDEC= []

    Rc2      = self.Rc**2
    power    = -3.0*beta+0.5

    self.SB0 = 1.0
 
    sigma    = 15.0*RtoD*self.Rc/self.d
#    tot_SB   = 0.0
    for i in range(sample_num):
       sRA = self.RA  + uniform(-sigma,sigma)
       sDEC= self.DEC + uniform(-sigma,sigma)
       sR2   = ((sRA-self.RA)**2 + (sDEC-self.DEC)**2)*(self.d*DtoR)**2
       if (sR2 < 144.0*Rc2):
          #S(r) = S_0 * ( 1 + (r/Rc)^2 )^(-3*beta+0.5)
          #self.sSB[i] = self.SB0*(1.0 + (sR/self.Rc)**2)**power
          self.sSB.append(( 1.0 + sR2/Rc2 )**power)
          self.sRA.append(sRA)
          self.sDEC.append(sDEC)

    if(len(self.sSB) <= Input_Para.samp_num_co*10):
       for i in range(Input_Para.samp_num_co*10):
         sRA = self.RA  + uniform(-sigma,sigma)
         sDEC= self.DEC + uniform(-sigma,sigma)
         sR2   = ((sRA-self.RA)**2 + (sDEC-self.DEC)**2)*(self.d*DtoR)**2
         self.sSB.append(( 1.0 + sR2/Rc2 )**power)
         self.sRA.append(sRA)
         self.sDEC.append(sDEC)

    flux_0 = 10.0**Halo_data.lgFx[sample_code]/len(self.sSB)
    for i in range(len(self.sSB[:])):
       self.sSB[i] = flux_0*self.sSB[i]

#   def add_sample_data(self,RA,DEC,Fx,Z_red):
#     self.RA       = RA
#     self.DEC      = DEC
#     self.Fx       = Fx
#     self.Z_red    = Z_red
#     self.Sample_nu= len(Fx[:])

