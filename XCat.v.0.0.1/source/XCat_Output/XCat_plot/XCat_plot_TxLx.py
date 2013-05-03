from numpy                       import zeros, log10, savetxt, array
from XCat_Objects                import pi
from matplotlib.pyplot           import *
from matplotlib                  import rc

rc('font',family='serif')

def plot_TxLx(Sliced_Halo_data,mode = 1):

    Sl_n  = len(Sliced_Halo_data)

    Z_max = max(Sliced_Halo_data[Sl_n-1].Z_red[:])

    clf()
    if (Sl_n != 1):
      for i in range(Sl_n):
         plot(Sliced_Halo_data[i].lgT,Sliced_Halo_data[i].lgLx,'.',color=(float(i)/float(Sl_n-1),0.0,1.0-float(i)/float(Sl_n-1)))
    else:
      plot(Sliced_Halo_data[0].lgT,Sliced_Halo_data[0].lgLx,'.b')

    #Plotting
    fdir  = './Output/plots/Tx-Lx/'
    rc('text',usetex=True)
    xlabel(r'$log(kT_X)~(keV)$',fontsize = 20)
    ylabel(r'$0.5-2~(keV)~log(L_X)~(10^{44}h_{0}^{-2}\erg~s^{-1})$',fontsize = 20)
    fname = 'TxLx_color'
    print 'Saving plot', fname, '.pdf'
    savefig(fdir+fname+'.pdf',dpi=200)
    rc('text',usetex=False)  
    close()
    print 'Saving data ', fname, '.txt'
    f = open(fdir+fname+'.txt','w')
    f.write("#          lgT                    lgLx\n")
    if (Sl_n != 1):
      for i in range(Sl_n):
         savetxt(f, array([Sliced_Halo_data[i].lgT,Sliced_Halo_data[i].lgLx]).T)
    else:
      savetxt(f, array([Sliced_Halo_data[0].lgT,Sliced_Halo_data[0].lgLx]).T)
    f.close()


    return 0
