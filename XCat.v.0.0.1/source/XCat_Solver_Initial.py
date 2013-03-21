#from XCat_Constants import ln10
from numpy   import log, exp, zeros
from XCat_Calculator                        import *
from XCat_Cosmology_Parameters              import Input_Parameters
from XCat_Model_Parameters_Rozo_et_al_2012  import Rozo_et_al_2012_Parameters
from XCat_Model_Parameters_Henry_et_al_2009 import Henry_et_al_2009_Parameters

ln10  = log(10)

# --- K-correction factors for [0.5-2.0 keV] band (Chris Mullis' 0.3 solar)
#   K1=  -0.209 + lgT*(1.181 - lgT*0.391)
#   K2=   -0.0988 + lgT*(-0.0924 + lgT*0.0851) 
# --- should read these from file
K1fac = [ -0.209 , 1.181   , -0.391 ] 
K2fac = [ -0.0988, -0.0924 , 0.0851 ]

#! -- make normal deviates (g)
def normal_dev(n):
   from random import random
   gdev   = zeros(n)
   gdevX  = zeros(n)
   i      = 0
   while (i<n):
      v1 = random()
      v2 = random()
      r  = v1**2 + v2**2
      if (r < 1.0 and r > 0.0):
        fac      = sqrt(-2.0*log(r)/r)
        gdev[i]  = v1*fac
        gdevx[i] = v2*fac
        i       += 1
   return (gdev,gdevx)

def Solver(Halo_data):

   Cosmology = Input_Parameters()
   
   n_data = len(Halo_data.X)
  
   #! --- set up Lx at nominal log-mean relation at z=0.23
   #Rozo_et_al_2012_Parameters
   Roza_Para = Rozo_et_al_2012_Parameters()
   #Henry_et_al_2009_Parameters
   Henry_Para= Henry_et_al_2009_Parameters()

   lgLxRo = zeros(n_data)
   lgLxbar= zeros(n_data)
   lghM15 = zeros(n_data)
   lgTbar = zeros(n_data) 
   print "DONE"

   for i in range(n_data):
      lnLxRo    = Roza_Para.a + Roza_Para.alpha * log(Halo_data.M500[i]/Roza_Para.mass)
      lgLxRo[i] = lnLxRo/ln10 
      lgLxbar[i]= lgLxRo[i] + Roza_Para.LxExPow * log10(Ez/EzRo)

      (Ez,EzRo) = Ev_factors(Cosmology.Omega_M,Cosmology.Omega_DE,Halo_data.Z_red[i])
      lghM15[i] = log10(Cosmology.h_0 * Ez * Halo_data.M500[i] / 10.0)
      lgTbar[i] = log10(Henry_Para.T_15) + Henry_Para.alpha_T*lghM15[i]
   print "DONE"

   (gdev,gdevx) = normal_dev(n_data)
   gdevT        = zeros(n_data)
   lnt          = zeros(n_data)
   lgT          = zeros(n_data)
   lnl          = zeros(n_data)
   lnlobs       = zeros(n_data)

   for i in range(n_data):
      #! ---- include correlation coefficient here
      gdevT[i]  = Cosmology.rTL*gdev + sqrt(1.0-Cosmology.rTL**2)*gdevX
      #! --- assign random temps w/ covariance (thru gdevT)
      lnt[i]    = ln10*lgTbar[i] + Henry_Para.siglnT*gdevT[i]
      Tx        = exp(lnt[i])
      lgT[i]    = log10(Tx)
      #! ---- random scatter in luminosities 
      lnl[i]    = ln10*lgLxbar[i] + Rozo_Para.siglnL*gdev[i]
      K1        = K1fac[0] + lgT[i]*(K1fac[1] + lgT[i]*K1fac[2])
      K2        = K2fac[0] + lgT[i]*(K2fac[1] + lgT[i]*K2fac[2])
      #! set LobsLrest = sqrt(1+ (1+log10(Tx/5))*zred)
      LobsLrest = 1.0 + Halo_data.Z_red[i]*(K1 + K2*Halo_data.Z_red[i])
      lnlobs[i] = lnl + Cosmology.K_corr*log(LobsLrest)
      #lnlbarobs = ln10*lgLxbar + $Kcorr*ln(LobsLrest)
   print "DONE"

   #! --- apply flux limit and extract data
   for i in range(n_data):
      fx = flux_cal(Halo_data.X[i],Halo_data.Y[i],Halo_data.Z[i],Halo_data.Z_red[i],Cosmology.h_0,lnlobs[i])
      if ( fx > Cosmology.Flim ):
        Halo_data.lnMT[i]     = -(Henry_Para.siglnT/Henry_Para.alpha_T) * gdevT[i]         
        Halo_data.lnML[i]     = -(Rozo_Para.siglnL/Rozo_Para.alpha)*gdev[i]                
        Halo_data.lgLx[i]     = lnl[i]/ln10                                                
        Halo_data.lgLxobs[i]  = lnlobs[i]/ln10                                             
        Halo_data.lgT[i]      = lnt[i]/ln10                                                
        Halo_data.lgfxf[i]    = log(fx)                                                    

   return Halo_data
