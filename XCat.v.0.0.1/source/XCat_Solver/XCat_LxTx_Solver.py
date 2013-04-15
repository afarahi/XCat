from numpy                      import log, log10, exp, sqrt, zeros
from XCat_Evolution_factor      import Evolution_factors
from XCat_Normal_Deviates       import normal_dev
from XCat_Objects               import fluxfac, ln10

def flux_cal(x,y,z,z_redshift,h_0,lnlobs): 
   #! --- convert comoving distance to Gpc for assumed h0
   r2     = ( x**2 + y**2 + z**2 ) / (1000.0*h_0)**2
   dlGpc2 = r2 * (1.0+z_redshift)**2
   fx = fluxfac * exp(lnlobs) / dlGpc2
   return fx

def LxTx_Solver(Sliced_Halo_data,InputParameters):
   '''
  if (mode == 0):
     n_data = Sliced_Halo_data.number_of_halos
  
     #! --- set up Lx at nominal log-mean relation at z=0.23
     #Lxm_Parameters
     Lxm_Para = InputParameters.Lxm_para_obj()
     #Txm_Parameters
     Txm_Para = InputParameters.Txm_para_obj()

     lgLx_i  = zeros(n_data)
     lgLxbar = zeros(n_data)
     lghM15  = zeros(n_data)
     lgTbar  = zeros(n_data)

     for i in range(n_data):

        (Ez,Ez_n) = Evolution_factors(InputParameters,Sliced_Halo_data.Z_red[i])
  
        lnLx      = Lxm_Para.a + Lxm_Para.alpha * log(Sliced_Halo_data.nM500[i]/Lxm_Para.mass)
        lgLx_i[i] = lnLx/ln10 
        lgLxbar[i]= lgLx_i[i] + Lxm_Para.LxEzPow * log10(Ez/Ez_n)

        lghM15[i] = log10(InputParameters.h_0 * Ez * Sliced_Halo_data.nM500[i] / 10.0)
        lgTbar[i] = log10(Txm_Para.T_15) + Txm_Para.alpha_T*lghM15[i]

     (gdev,gdevX) = normal_dev(n_data)
     gdevT        = zeros(n_data)
     lnt          = zeros(n_data)
     lgT          = zeros(n_data)
     lnl          = zeros(n_data)
     lnlobs       = zeros(n_data)

     for i in range(n_data):
        #! ---- include correlation coefficient here
        gdevT[i]  = InputParameters.rTL*gdev[i] + sqrt(1.0-InputParameters.rTL**2)*gdevX[i]
        #! --- assign random temps w/ covariance (thru gdevT)
        lnt[i]    = ln10*lgTbar[i] + Txm_Para.siglnT*gdevT[i]
#      Tx        = exp(lnt[i])
#      lgT[i]    = log10(Tx)
        lgT[i]    = lnt[i]/ln10
      #! ---- random scatter in luminosities 
        lnl[i]    = ln10*lgLxbar[i] + Lxm_Para.siglnL*gdev[i]
        K1        = InputParameters.K1fac[0] + lgT[i]*(InputParameters.K1fac[1] + lgT[i]*InputParameters.K1fac[2])
        K2        = InputParameters.K2fac[0] + lgT[i]*(InputParameters.K2fac[1] + lgT[i]*InputParameters.K2fac[2])
      #! set LobsLrest = sqrt(1+ (1+log10(Tx/5))*zred)
        LobsLrest = 1.0 + Sliced_Halo_data.Z_red[i]*(K1 + K2*Sliced_Halo_data.Z_red[i])
        lnlobs[i] = lnl[i] + InputParameters.K_corr*log(LobsLrest)
      #lnlbarobs = ln10*lgLxbar + $Kcorr*ln(LobsLrest)

     #! --- apply flux limit and extract data
     for i in range(n_data):
        fx = flux_cal(Sliced_Halo_data.X[i],Sliced_Halo_data.Y[i],Sliced_Halo_data.Z[i],Sliced_Halo_data.Z_red[i],InputParameters.h_0,lnlobs[i])
#      if ( fx > InputParameters.Flim ):
        Sliced_Halo_data.lnMT[i]     = -(Txm_Para.siglnT/Txm_Para.alpha_T) * gdevT[i]         
        Sliced_Halo_data.lnML[i]     = -(Lxm_Para.siglnL/Lxm_Para.alpha) * gdev[i]                
        Sliced_Halo_data.lgLx[i]     = lnl[i]/ln10
#      print Sliced_Halo_data.lgLx[i]                                                
        Sliced_Halo_data.lgLxobs[i]  = lnlobs[i]/ln10                                             
        Sliced_Halo_data.lgT[i]      = lgT[i]                                               
        Sliced_Halo_data.lgFx[i]     = log10(fx)                                                    
  elif(mode == 1):
   '''
   Sl_n  = len(Sliced_Halo_data)
   for k in range(Sl_n):

     n_data = Sliced_Halo_data[k].number_of_halos
  
     #! --- set up Lx at nominal log-mean relation at z=0.23
     #Lxm_Parameters
     Lxm_Para = InputParameters.Lxm_para_obj()
     #Txm_Parameters
     Txm_Para = InputParameters.Txm_para_obj()

     lgLx_i  = zeros(n_data)
     lgLxbar = zeros(n_data)
     lghM15  = zeros(n_data)
     lgTbar  = zeros(n_data)

     for i in range(n_data):

        (Ez,Ez_n) = Evolution_factors(InputParameters,Sliced_Halo_data[k].Z_red[i])
  
        lnLx      = Lxm_Para.a + Lxm_Para.alpha * log(Sliced_Halo_data[k].nM500[i]/Lxm_Para.mass)
        lgLx_i[i] = lnLx/ln10 
        lgLxbar[i]= lgLx_i[i] + Lxm_Para.LxEzPow * log10(Ez/Ez_n)

        lghM15[i] = log10(InputParameters.h_0 * Ez * Sliced_Halo_data[k].nM500[i] / 10.0)
        lgTbar[i] = log10(Txm_Para.T_15) + Txm_Para.alpha_T*lghM15[i]

     (gdev,gdevX) = normal_dev(n_data)
     gdevT        = zeros(n_data)
     lnt          = zeros(n_data)
     lgT          = zeros(n_data)
     lnl          = zeros(n_data)
     lnlobs       = zeros(n_data)

     for i in range(n_data):
        #! ---- include correlation coefficient here
        gdevT[i]  = InputParameters.rTL*gdev[i] + sqrt(1.0-InputParameters.rTL**2)*gdevX[i]
        #! --- assign random temps w/ covariance (thru gdevT)
        lnt[i]    = ln10*lgTbar[i] + Txm_Para.siglnT*gdevT[i]
#      Tx        = exp(lnt[i])
#      lgT[i]    = log10(Tx)
        lgT[i]    = lnt[i]/ln10
      #! ---- random scatter in luminosities 
        lnl[i]    = ln10*lgLxbar[i] + Lxm_Para.siglnL*gdev[i]
        K1        = InputParameters.K1fac[0] + lgT[i]*(InputParameters.K1fac[1] + lgT[i]*InputParameters.K1fac[2])
        K2        = InputParameters.K2fac[0] + lgT[i]*(InputParameters.K2fac[1] + lgT[i]*InputParameters.K2fac[2])
      #! set LobsLrest = sqrt(1+ (1+log10(Tx/5))*zred)
        LobsLrest = 1.0 + Sliced_Halo_data[k].Z_red[i]*(K1 + K2*Sliced_Halo_data[k].Z_red[i])
        lnlobs[i] = lnl[i] + InputParameters.K_corr*log(LobsLrest)
      #lnlbarobs = ln10*lgLxbar + $Kcorr*ln(LobsLrest)

     #! --- apply flux limit and extract data
     for i in range(n_data):
        fx = flux_cal(Sliced_Halo_data[k].X[i],Sliced_Halo_data[k].Y[i],Sliced_Halo_data[k].Z[i],Sliced_Halo_data[k].Z_red[i],InputParameters.h_0,lnlobs[i])
#      if ( fx > InputParameters.Flim ):
        Sliced_Halo_data[k].lnMT[i]     = -(Txm_Para.siglnT/Txm_Para.alpha_T) * gdevT[i]         
        Sliced_Halo_data[k].lnML[i]     = -(Lxm_Para.siglnL/Lxm_Para.alpha) * gdev[i]                
        Sliced_Halo_data[k].lgLx[i]     = lnl[i]/ln10
#      print Sliced_Halo_data[k].lgLx[i]                                                
        Sliced_Halo_data[k].lgLxobs[i]  = lnlobs[i]/ln10                                             
        Sliced_Halo_data[k].lgT[i]      = lgT[i]                                               
        Sliced_Halo_data[k].lgFx[i]     = log10(fx)                                                    

   print "Fluxes, Tempratures, and Luminosities are computed successfully." 

   return Sliced_Halo_data
