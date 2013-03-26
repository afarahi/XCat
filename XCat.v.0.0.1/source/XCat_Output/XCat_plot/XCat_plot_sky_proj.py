from numpy                       import linspace, zeros, sin, cos, log, exp
from XCat_Objects                import pi
from matplotlib.pyplot           import *
from matplotlib                  import rc

rc('font',family='serif')

def plot_sky_projection(Halo_data):

    n = Halo_data.number_of_halos
    Z_max = max(Halo_data.Z_red)

    for i in range(n):
      theta = (pi/180.0)*(90.0-Halo_data.DEC[i])
      RA    = Halo_data.RA[i] - 90.0
      DEC   = Halo_data.DEC[i]
      Z_red = Halo_data.Z_red[i]
      
      figure(1)
      if (Z_red <= 0.3):
         plot(sin(theta)*RA,DEC,'b.')
      elif (Z_red <= 0.6):
         plot(sin(theta)*RA,DEC,'g.')
      else:
         plot(sin(theta)*RA,DEC,'r.')
      figure(2)
      plot(sin(theta)*RA,DEC,'.',color=[Z_red/Z_max,0.0,1.0-Z_red/Z_max])

    #Plotting
    fdir  = './Output/plots/'
    fname = 'sky_projection_color_v1.png'
    print 'Saving plot', fname
    savefig(fdir+fname)

    rc('text',usetex=True)
    figure(1)
    title(r'$1/4$ sky projection',fontsize = 20)
    fname = 'sky_projection_color_v2.pdf'
    print 'Saving plot', fname
    savefig(fdir+fname)
    rc('text',usetex=False)  

    return 0

#    xlabel(r'$\omega$',fontsize = 20)
#    ylabel(r'$P(\omega)$',fontsize = 20)

