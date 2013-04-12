from numpy                      import log, log10, exp, sqrt, zeros
from XCat_Utilities             import Read_Integer_Input
from XCat_Objects               import Halo_Sample_Object

def flux_cal(r,z_redshift,h_0,lnlobs): 
   #! --- convert comoving distance to Gpc for assumed h0
   r2     = ( r**2 ) / (1000.0*h_0)**2
   dlGpc2 = r2 * (1.0+z_redshift)**2
   fx = fluxfac * exp(lnlobs) / dlGpc2
   return fx

def Surface_Brightness_Solver_beta_model(RA,DEC,Rc,d_l,Fx):
    from random import gauss
    n    = 10
    beta = 0.5

    flux_sample = zeros(n)
    RA_sample   = zeros(n)
    DEC_sample  = zeros(n)

    for i in range(n):
       RA_sample[i] = gauss(RA,0.1)
       DEC_sample[i]= gauss(DEC,0.1)
       R            = d_l*(DtoR*sqrt((RA_sample[i]-RA)**2 + (DEC_sample[i]-DEC)**2))
       Fx_sample[i] = Fx*(1.0 + (R/Rc)**2)**(-3.0*beta+0.5)

    return (RA_sample,DEC_sample,Fx_sample)

def Surface_Brightness_Solver(Halo_data):

    Sl_n  = len(Halo_data)
    k = Read_Integer_Input("We have %i redshift slice  which one you want exctract the halo ? "%Sl_n)
    k = int(k) - 1
    while(k > (Sl_n-1) or k < 0 ):
      print "Invalid Number."
      k = Read_Integer_Input("Please choose an integer between 1 and %i : "%Sl_n)
      k = int(k) - 1
    n       = len(Halo_data[k].RA[:])
    halo_n = Read_Integer_Input("We have %i halos in this slice which one you want to exctract ? "%n)
    d_l    = (Halo_data[k].X[halo_n]**2 + Halo_data[k].Y[halo_n]**2 + Halo_data[k].Z[halo_n]**2)
    (RA_sample,DEC_sample,Fx_sample) = Surface_Brightness_Solver_beta_model(Halo_data[k].RA[halo_n],Halo_data[k].DEC[halo_n],Rc,d_l,10**Halo_data[k].lgFx[halo_n])

    Halo_Sample = Halo_Sample_Object()
    Halo_Sample.add_sample_data(RA_sample,DEC_sample,Fx_sample,Halo_data[k].Z_red[halo_n])
