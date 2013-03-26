from numpy                             import log, log10
from XCat_Celestial_Coordinate_System  import EquatorialTOGalactic

class Halo_Object():

   def __init__(self,Halos_info,Input_Param):

     self.X        = []
     self.Y        = []
     self.Z        = []

     self.RA       = []
     self.DEC      = []
     self.gLong    = []
     self.gLati    = []

     self.M500     = []
     self.nM500    = []

     self.Z_red    = []

     self.lgT      = []
     self.lnMT     = []
     self.lnML     = []
     self.lgLx     = []
     self.lgFx     = []
     self.lgLxobs  = []
     
     n = len(Halos_info.field('HALOPX')[:])

     counter = 0

     for i in range(n):
       if(Halos_info.field('M200')[i] > Input_Param.Mlim):
          self.X.append(Halos_info.field('HALOPX')[i])
          self.Y.append(Halos_info.field('HALOPY')[i])
          self.Z.append(Halos_info.field('HALOPZ')[i])

          self.RA.append(Halos_info.field('RA')[i])
          self.DEC.append(Halos_info.field('DEC')[i])
          (gLong,gLati) = EquatorialTOGalactic(Halos_info.field('RA')[i],Halos_info.field('DEC')[i])
          self.gLong.append(gLong)
          self.gLati.append(gLati)
#          print "RA = ", self.RA[counter] , "  DEC = ", self.DEC[counter]

          M500 = Halos_info.field('M200')[i]/1.4
          self.M500.append(M500)
          #normalized mass
          self.nM500.append(M500/(Input_Param.h_0*1e14))          
#          self.M500.append(Halos_info.field('M500')[i])

          self.Z_red.append(Halos_info.field('Z')[i])

          self.lgT.append(0.0)
          self.lnMT.append(0.0)
          self.lnML.append(0.0)
          self.lgLx.append(0.0)
          self.lgFx.append(0.0)
          self.lgLxobs.append(0.0)
          
          counter += 1
   
     self.number_of_halos = counter     

     print "Number of Halos = ", counter
     print "HALOS INITIALIZED SUCCESSFULLY."

