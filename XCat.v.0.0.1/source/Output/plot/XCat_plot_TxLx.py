from XCat_Conversions_Constants  import pi
from numpy                       import linspace, zeros, sin, cos, log, exp
from matplotlib.pyplot           import *
from matplotlib                  import rc

rc('font',family='serif')

def plot_TxLx(Halo_data):

    n = Halo_data.number_of_halos
    Z_max = max(Halo_data.Z_red)
    for i in range(n):
      plot(Halo_data.lgT[i],Halo_data.lgFx[i],'.')#,color=[Halo_data.Z_red[i]/Z_max,0.0,1.0-Halo_data.Z_red[i]/Z_max])

    #Plotting
    fdir  = './Output/plots/'
    rc('text',usetex=True)
    xlabel(r'$kT_X~(keV)$',fontsize = 20)
    ylabel(r'$0.5-2~keV~L_X~(10^{44}h_{0}^{-2}\erg~s^{-1})$',fontsize = 20)
    fname = 'TxLx_color_v1.pdf'
    print 'Saving plot', fname
    savefig(fdir+fname)
    rc('text',usetex=False)  

    return 0
