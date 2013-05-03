from XCat_Utilities import read_data_string
import pyfits

def Read_Halo_Cat_fit(file_name = None):
    if (file_name == None):
       file_name    = read_data_string(tag_name = 'File_name' , file_name = 'parameters/Input_Parameters.xml')
    file_address = 'Catalog/Input_File/' + file_name
    print "Reading Halo Catalog ..."
    try:
       Halos_list = pyfits.open(file_address)
       Halos_list.info()
       Halos_head = Halos_list[1].header
       Halos_info = Halos_list[1].data
       print "Reading Halo Catalog is done."
    except IOError:
       print "Error: can\'t find file or read data"
       raw_input("Press enter to continue ... ")
       return False
#    Halos_info = Halos_list[1].data[1:50000]
#    print "DONE"
#    pyfits.writeto('new.fit',Halos_info,Halos_head)
#    print Halos_info.field('HALOPX')[2]
#    print Halos_info[2][17]
    return Halos_info

#HALO FILE STRUCTURE:

#     ['HALOID', 'M200', 'R200', 'M200B', 'R200B', 'M500', 'R500', 'MVIR', 'RVIR', 'M2500', 'R2500', 'VRMS', 'RS', 'JX', 'JY', 'JZ', 'SPIN', 'HALOPX', 'HALOPY', 'HALOPZ', 'HALOVX', 'HALOVY', 'HALOVZ', 'LUMTOT', 'LUM20', 'LBCG', 'RA', 'DEC', 'Z', 'NGALS', 'N18', 'N19', 'N20', 'N21', 'N22', 'EDGE', 'HOST_HALOID', 'XOFF', 'VOFF', 'LAMBDA', 'B_TO_A', 'C_TO_A', 'AX', 'AY', 'AZ', 'VIRIAL_RATIO']

#Catalog Tags: halo files
#halos for this catalog were found using the ROCKSTAR halo finder.
#current version extends to z = 2. note that the halo catalog is constructed from three simulations and has a different mass limit in these 3 simulations (lower at lower redshift).

# 0   * HALOID: A unique id # for that halo
# 1   * M200: Halo mass, M_200,crit [Msun/h]
# 2   * R200: Halo radius, R_200,crit [Mpc/h], physical
# 3   * M200b: Halo mass, M_200,background [Msun/h]
# 4   * R200b: Halo radius, R_200,background [Mpc/h], physical
# 5   * M500: Halo mass, M_500,crit [Msun/h]
# 6   * R500: Halo radius, R_500,crit [Mpc/h], physical
# 7   * MVIR: Halo mass, M_vir [Msun/h]
# 8   * RVIR: Halo radius, R_vir [Mpc/h], physical
# 9   * M2500: Halo mass, M_2500,crit [Msun/h] *** warning, may not be well resolved
# 10  * R2500: Halo radius, R_2500,crit [Mpc/h], physical *** warning, may not be well resolved
# 11  * VRMS: 3D velocity dispersion of particles in the halo
# 12  * RS: Halo scale radius
# 13  * J[X,Y,Z]: Halo angular momentum
# 14  * SPIN: Halo spin
# 15  * HALO[PX,PY,PZ]: halo position [Mpc/h]
# 16  * HALO[VX,VY,VZ]: halo velocity [km/s]
# 17  * LUMTOT: Total DES r-band luminosity of all galaxies within R200
# 18  * LUM20: Total DES r-band luminosity of all galaxies brighter than Mr -5logh = -20 within R200
# 19  * LBCG: r-band luminosity of the central galaxy in the halo
# 20  * RA: halo right ascension
# 21  * DEC: halo declination
# 22  * Z: halo redshift (including peculiar velocities)
# 23  * NGALS: total number of galaxies within R200 of the halo center
# 24  * N18: number of galaxies within R200 brigher than Mr -5logh = -18
# 25  * N19: number of galaxies within R200 brigher than Mr -5logh = -19
# 26  * N20: number of galaxies within R200 brigher than Mr -5logh = -20
# 27  * N21: number of galaxies within R200 brigher than Mr -5logh = -21
# 28  * N22: number of galaxies within R200 brigher than Mr -5logh = -22
# 29  * EDGE: boolean flag indicating whether the halo is on an edge (set to zero for all halos in this version)
# 30  * HOST_HALOID: HALOID of the host halo for subhalos, set to HALOID of this halo for central halos
# 31  * XOFF:
# 32  * VOFF:
# 33  * LAMBDA: halo spin parameter
# 34  * B_TO_A: halo shape parameter
# 35  * C_TO_A: halo shape parameter
# 36  * A[X,Y,Z]: halo triaxiality
# 37  * VIRIAL_RATIO: 
