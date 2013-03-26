from numpy                       import zeros, log10
from XCat_Objects                import pi
from matplotlib.pyplot           import *
from matplotlib                  import rc

rc('font',family='serif')

def plot_TxLx(Halo_data):

    n = Halo_data.number_of_halos
    Z_max = max(Halo_data.Z_red)
    
    plot(Halo_data.lgT,Halo_data.lgLx,'.b')

#    for i in range(n): 
#      plot(Halo_data.lgT[i],Halo_data.lgLx[i],'.',color=[Halo_data.Z_red[i]/Z_max,0.0,1.0-Halo_data.Z_red[i]/Z_max])

    #Plotting
    fdir  = './Output/plots/'
    rc('text',usetex=True)
    xlabel(r'$kT_X~(keV)$',fontsize = 20)
    ylabel(r'$0.5-2~(keV)~L_X~(10^{44}h_{0}^{-2}\erg~s^{-1})$',fontsize = 20)
    fname = 'TxLx_color_v1.pdf'
    print 'Saving plot', fname
    savefig(fdir+fname)
    rc('text',usetex=False)  

    return 0
