#from numpy  import log, log10, zeros

class Halo_Sample_Object():

   def __init__(self):
     self.Fx       = []
     self.RA       = []
     self.DEC      = []

     self.Z_red    = []

   def add_sample_data(self,RA,DEC,Fx,Z_red):
     self.RA       = RA
     self.DEC      = DEC
     self.Fx       = Fx

     self.Z_red    = Z_red
 
     self.Sample_nu= len(Fx[:])

