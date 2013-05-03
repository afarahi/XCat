from numpy                      import linspace, zeros, sqrt, cos, log10
from XCat_Utilities             import Read_Integer_Input
from XCat_Objects               import DtoR
import healpy                     as hp

def mass_function_Solver(Sliced_Halo_data,k,Input_Param):

    min_logmass = log10(Input_Param.Mlim)
    max_logmass = 15.0
    n_logdmass  = 21

    n_data = Sliced_Halo_data[k].number_of_halos

    logmass= linspace(min_logmass,max_logmass,n_logdmass)

    mfm500 = zeros(len(logmass))
    for i in range(n_data):
       for j in range(1,len(logmass)):
          if ( (10.0**logmass[j-1] <= Sliced_Halo_data[k].M500[i]) ):
             mfm500[j] += 1

    dRA    = DtoR*max(Sliced_Halo_data[k].RA[:]) - min(Sliced_Halo_data[k].RA[:]) 
    DEC_min= DtoR*( 90.0-min(Sliced_Halo_data[k].DEC[:]) )
    DEC_max= DtoR*( 90.0-max(Sliced_Halo_data[k].DEC[:]) )
#    z_max  = max(Sliced_Halo_data[k].Z_red[:])
#    r_max  = sqrt( Sliced_Halo_data[k].X[z_max]**2 + Sliced_Halo_data[k].Y[z_max]**2 + Sliced_Halo_data[k].Z[z_max]**2 )
#    z_min  = max(Sliced_Halo_data[k].Z_red[:])
#    r_min  = sqrt( Sliced_Halo_data[k].X[z_min]**2 + Sliced_Halo_data[k].Y[z_min]**2 + Sliced_Halo_data[k].Z[z_min]**2 )
    r_max  = sqrt( max(Sliced_Halo_data[k].r2[:]) )
    r_min  = sqrt( min(Sliced_Halo_data[k].r2[:]) )

    #NEED TO DIVIDE IT BY VOLUME !! int dr [int d theta [int d phi[ sin(theta) r^2 ]]] 
    # =  (phi_2 - phi_1) * (Cos(theta_2)-Cos(theta_2)) * (r_2^3 - r_1^3) / 3
    vol = abs(dRA * (cos(DEC_max) - cos(DEC_min)) * (r_max**3 - r_min**3) / 3.0)
    for j in range(1,len(logmass)):
       mfm500[j] = mfm500[j]/vol

    #Unites N (>M) (1/h^3 Mpc^3) , M (Msun/h) 
    print "mass function is : "
    for j in range(1,len(logmass)):
       print logmass[j], mfm500[j]

    print "mass function is computed successfully." 

    return (logmass,mfm500)
