from XCat_Utilities             import Read_Integer_Input, Read_YN_Input
from numpy                      import log, log10, exp, sqrt, zeros, savetxt, array
from matplotlib                 import rc
import matplotlib.pyplot         as plt

def plot_mass_function(Halo_data,Input_Param,Output_Param,General_Prop):

    from XCat_mass_function_Solver  import mass_function_Solver

    rc('font',family='serif')
    fdir  = './Output/plots/mass_function/'

    Sl_n  = len(Halo_data)

    for k in range(Sl_n):
      if (len(Halo_data[k].RA[:]) <= 10):
         print "There is not enough data to creat mass function of redshift between %0.3f and %0.3f"%(Halo_data[k].z_min,Halo_data[k].z_max)
         pass 
      else:
         (log_m,mfm500) = mass_function_Solver(Halo_data,k,Input_Param)

         for i in range(len(log_m)):
             log_m[i] = 10.0**log_m[i]

         plt.clf()
         rc('text',usetex=True)
         plt.loglog(log_m,mfm500)
         plt.xlabel(r'$M_{500}~~~h^{-1}~M_{\odot}$')
         plt.ylabel(r'$N(>M_{500})~~~h^{-3}~Mpc^{-3}$ ')
         fname = 'Mass_function_%i'%(k+1)
         plt.title(r'Mass function of redshift between %0.3f and %0.3f'%(Halo_data[k].z_min,Halo_data[k].z_max),fontsize = 20)
         print 'Saving plot', fname, '.pdf'
         plt.savefig(fdir+fname+'.pdf',bbox_inches='tight')
         rc('text',usetex=False)

         print 'Saving data', fname, '.txt'
         f = open(fdir+fname+'.txt','w')
         f.write("#      m_500               mass function m_500\n")
         savetxt(f, array([log_m, mfm500]).T)
         f.close()

         plt.close()
    del Sl_n, log_m, mfm500, fdir, fname
