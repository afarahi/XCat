from numpy  import log, log10, zeros
'''
class Halo_Object():

   def __init__(self,Halos_info = None,Input_Param = None,General_Prop = None):
     
     self.X        = []
     self.Y        = []
     self.Z        = []

     self.RA       = []
     self.DEC      = []

     self.R200     = []
     self.M200     = []
     self.M500     = []
     self.nM500    = []

     self.Z_red    = []

     self.lgT      = []
     self.lnMT     = []
     self.lnML     = []
     self.lgLx     = []
     self.lgFx     = []
     self.lgLxobs  = []

     if (Halos_info != None):
        n = len(Halos_info.field('HALOPX')[:])
        for i in range(n):
          if(Halos_info.field('M200')[i]/1.4 > Input_Param.Mlim):
             self.X.append(Halos_info.field('HALOPX')[i])
             self.Y.append(Halos_info.field('HALOPY')[i])
             self.Z.append(Halos_info.field('HALOPZ')[i])

             self.RA.append(Halos_info.field('RA')[i])     
             self.DEC.append(Halos_info.field('DEC')[i])

             self.R200.append(Halos_info.field('R200')[i])
             self.M200.append(Halos_info.field('M200')[i])
             M500 = Halos_info.field('M200')[i]/1.4
             self.M500.append(M500)
             #normalized mass
             self.nM500.append(M500/(1e14))          
#             self.M500.append(Halos_info.field('M500')[i])

             red_shift = Halos_info.field('Z')[i]
             self.Z_red.append(red_shift)
   
             self.lgT.append(0.0)
             self.lnMT.append(0.0)
             self.lnML.append(0.0)
             self.lgLx.append(0.0)
             self.lgFx.append(0.0)
             self.lgLxobs.append(0.0)
 
        self.number_of_halos =  len(self.Z_red[:])

        General_Prop.update(self)

        print "Number of Halos = ", self.number_of_halos
        print "HALOS INITIALIZED SUCCESSFULLY."
        raw_input("Press enter to continue ... ")

   def add_new_catalog(self,Halos_info,Input_Param):

     n = len(Halos_info.field('HALOPX')[:])

     for i in range(n):
       if(Halos_info.field('M200')[i] > Input_Param.Mlim):
          self.X.append(Halos_info.field('HALOPX')[i])
          self.Y.append(Halos_info.field('HALOPY')[i])
          self.Z.append(Halos_info.field('HALOPZ')[i])

          self.RA.append(Halos_info.field('RA')[i])     
          self.DEC.append(Halos_info.field('DEC')[i])

          self.R200.append(Halos_info.field('R200')[i])
          self.M200.append(Halos_info.field('M200')[i])
          M500 = Halos_info.field('M200')[i]/1.4
          self.M500.append(M500)
          #normalized mass
          self.nM500.append(M500/(1e14))          

          red_shift = Halos_info.field('Z')[i]
          self.Z_red.append(red_shift)

          self.lgT.append(0.0)
          self.lnMT.append(0.0)
          self.lnML.append(0.0)
          self.lgLx.append(0.0)
          self.lgFx.append(0.0)
          self.lgLxobs.append(0.0)
            
     self.number_of_halos = len(self.Z_red[:])

     self.z_min  = min(self.Z_red[:])
     self.z_max  = max(self.Z_red[:])

     General_Prop.update(self)

     print "Number of Halos = ", self.number_of_halos
     print "HALOS ADDED SUCCESSFULLY."
     raw_input("Press enter to continue ... ")


   def redshift_org(self,Input_Param):
     n = len(self.Z_red[:])
     self.max_Z    = max(self.Z_red[:])

     self.Z_slice  = Input_Param.red_shift_n
     self.Z_group_n= []     
     self.Z_group_halo_counter= zeros([self.Z_slice],dtype=int)     
     
     for i in range(n):
          red_shift = self.Z_red[i]
          for j in range(self.Z_slice):
             if ( (float(j)*self.max_Z/float(self.Z_slice)) < red_shift):
                if (red_shift <= (float(j+1)*self.max_Z/float(self.Z_slice)) ):
                   self.Z_group_halo_counter[j] += 1
                   self.Z_group_n.append(j)      
                   break


   def add_single_data(self,Halos_data,i):
       self.X.append(Halos_data.X[i])
       self.Y.append(Halos_data.Y[i])
       self.Z.append(Halos_data.Z[i])
       self.RA.append(Halos_data.RA[i])
       self.DEC.append(Halos_data.DEC[i])
       self.R200.append(Halos_data.R200[i])
       self.M200.append(Halos_data.R200[i])
       self.M500.append(Halos_data.M500[i])
       self.nM500.append(Halos_data.nM500[i])
       self.Z_red.append(Halos_data.Z_red[i])
       self.lgT.append(Halos_data.lgT[i])
       self.lgLx.append(Halos_data.lgLx[i])
       self.lgFx.append(Halos_data.lgFx[i])
       self.lnMT.append(Halos_data.lnMT[i])
       self.lnML.append(Halos_data.lnML[i])
       self.lgLxobs.append(Halos_data.lgLxobs[i])

   def update_halo_data(self):
       self.number_of_halos = len(self.Z_red[:])
       print "Number of Halos : ", self.number_of_halos
       General_Prop.update(self)
'''
'''
class Halo_Object():

   def __init__(self,Halos_info = None,Input_Param = None,General_Prop = None):
     
     if (Halos_info != None):

        self.X        = list(Halos_info.field('HALOPX'))
        self.Y        = list(Halos_info.field('HALOPY'))
        self.Z        = list(Halos_info.field('HALOPZ'))

        self.RA       = list(Halos_info.field('RA'))
        self.DEC      = list(Halos_info.field('DEC'))

        self.R200     = list(Halos_info.field('R200'))
        self.M200     = list(Halos_info.field('M200'))
        self.M500     = list(Halos_info.field('M500'))
        self.nM500    = list(Halos_info.field('M200')/(1e14))

        self.Z_red    = list(Halos_info.field('Z'))
     
        i = 0
        while (i < len(self.M200[:])) :
          if(self.M200[i]/1.4 < Input_Param.Mlim):
             self.X.pop(i)
             self.Y.pop(i)
             self.Z.pop(i)
             self.RA.pop(i)     
             self.DEC.pop(i)
             self.R200.pop(i)
             self.M200.pop(i)
             self.M500.pop(i)
             self.nM500.pop(i)
             self.Z_red.pop(i)
          else:
             i += 1

        n = len(self.M200[:])
        self.lgT      = list(zeros(n))
        self.lnMT     = list(zeros(n))
        self.lnML     = list(zeros(n))
        self.lgLx     = list(zeros(n))
        self.lgFx     = list(zeros(n))
        self.lgLxobs  = list(zeros(n))
 
        self.number_of_halos =  len(self.Z_red[:])

        General_Prop.update(self)

        print "Number of Halos = ", self.number_of_halos
        print "HALOS INITIALIZED SUCCESSFULLY."
        raw_input("Press enter to continue ... ")
     else:
        self.X        = []
        self.Y        = []
        self.Z        = []
  
        self.RA       = []
        self.DEC      = []

        self.R200     = []
        self.M200     = []
        self.M500     = []
        self.nM500    = []
  
        self.Z_red    = []
 
        self.lgT      = []
        self.lnMT     = []
        self.lnML     = []
        self.lgLx     = []
        self.lgFx     = []
        self.lgLxobs  = []
 
   def add_new_catalog(self,Halos_info,Input_Param):

     n = len(Halos_info.field('HALOPX')[:])

     for i in range(n):
       if(Halos_info.field('M200')[i] > Input_Param.Mlim):
          self.X.append(Halos_info.field('HALOPX')[i])
          self.Y.append(Halos_info.field('HALOPY')[i])
          self.Z.append(Halos_info.field('HALOPZ')[i])

          self.RA.append(Halos_info.field('RA')[i])     
          self.DEC.append(Halos_info.field('DEC')[i])

          self.R200.append(Halos_info.field('R200')[i])
          self.M200.append(Halos_info.field('M200')[i])
          M500 = Halos_info.field('M200')[i]/1.4
          self.M500.append(M500)
          #normalized mass
          self.nM500.append(M500/(1e14))          

          red_shift = Halos_info.field('Z')[i]
          self.Z_red.append(red_shift)

          self.lgT.append(0.0)
          self.lnMT.append(0.0)
          self.lnML.append(0.0)
          self.lgLx.append(0.0)
          self.lgFx.append(0.0)
          self.lgLxobs.append(0.0)
            
     self.number_of_halos = len(self.Z_red[:])

     self.z_min  = min(self.Z_red[:])
     self.z_max  = max(self.Z_red[:])

     General_Prop.update(self)

     print "Number of Halos = ", self.number_of_halos
     print "HALOS ADDED SUCCESSFULLY."
     raw_input("Press enter to continue ... ")


   def redshift_org(self,Input_Param):
     n = len(self.Z_red[:])
     self.max_Z    = max(self.Z_red[:])

     self.Z_slice  = Input_Param.red_shift_n
     self.Z_group_n= []     
     self.Z_group_halo_counter= zeros([self.Z_slice],dtype=int)     
     
     for i in range(n):
          red_shift = self.Z_red[i]
          for j in range(self.Z_slice):
             if ( (float(j)*self.max_Z/float(self.Z_slice)) < red_shift):
                if (red_shift <= (float(j+1)*self.max_Z/float(self.Z_slice)) ):
                   self.Z_group_halo_counter[j] += 1
                   self.Z_group_n.append(j)      
                   break


   def add_single_data(self,Halos_data,i):
       self.X.append(Halos_data.X[i])
       self.Y.append(Halos_data.Y[i])
       self.Z.append(Halos_data.Z[i])
       self.RA.append(Halos_data.RA[i])
       self.DEC.append(Halos_data.DEC[i])
       self.R200.append(Halos_data.R200[i])
       self.M200.append(Halos_data.R200[i])
       self.M500.append(Halos_data.M500[i])
       self.nM500.append(Halos_data.nM500[i])
       self.Z_red.append(Halos_data.Z_red[i])
       self.lgT.append(Halos_data.lgT[i])
       self.lgLx.append(Halos_data.lgLx[i])
       self.lgFx.append(Halos_data.lgFx[i])
       self.lnMT.append(Halos_data.lnMT[i])
       self.lnML.append(Halos_data.lnML[i])
       self.lgLxobs.append(Halos_data.lgLxobs[i])

   def update_halo_data(self):
       self.number_of_halos = len(self.Z_red[:])
       print "Number of Halos : ", self.number_of_halos
       General_Prop.update(self)
'''

class Halo_Object():

   def __init__(self,Halos_info = None,Input_Param = None,General_Prop = None):

     self.X        = []
     self.Y        = []
     self.Z        = []

     self.RA       = []
     self.DEC      = []

     self.R200     = []
     self.M200     = []
     self.M500     = []
     self.nM500    = []

     self.Z_red    = []

     self.lgT      = []
     self.lnMT     = []
     self.lnML     = []
     self.lgLx     = []
     self.lgFx     = []
     self.lgLxobs  = []
     
     if (Halos_info != None):
        for i in  range(len(Halos_info[:])):
          if(Halos_info[i][1]/1.4 > Input_Param.Mlim):
             self.X.append(Halos_info[i][17])
             self.Y.append(Halos_info[i][18])
             self.Z.append(Halos_info[i][19])
             self.RA.append(Halos_info[i][26])     
             self.DEC.append(Halos_info[i][27])
             self.R200.append(Halos_info[i][2])
             self.M200.append(Halos_info[i][1])
             self.M500.append(Halos_info[i][1]/1.4)
             self.nM500.append(Halos_info[i][1]/(1.4*1e14))
             self.Z_red.append(Halos_info[i][28])
          else:
             i += 1
          if (i%100000 == 0):
             print " Halo number : " , i

        n = len(self.M200[:])
        self.lgT      = list(zeros(n))
        self.lnMT     = list(zeros(n))
        self.lnML     = list(zeros(n))
        self.lgLx     = list(zeros(n))
        self.lgFx     = list(zeros(n))
        self.lgLxobs  = list(zeros(n))
 
        self.number_of_halos =  len(self.Z_red[:])

        General_Prop.update(self)

        print "Number of Halos = ", self.number_of_halos
        print "HALOS INITIALIZED SUCCESSFULLY."
        raw_input("Press enter to continue ... ")

 
   def add_new_catalog(self,Halos_info,Input_Param):

     n = len(Halos_info.field('HALOPX')[:])

     for i in range(n):
       if(Halos_info.field('M200')[i] > Input_Param.Mlim):
          self.X.append(Halos_info.field('HALOPX')[i])
          self.Y.append(Halos_info.field('HALOPY')[i])
          self.Z.append(Halos_info.field('HALOPZ')[i])

          self.RA.append(Halos_info.field('RA')[i])     
          self.DEC.append(Halos_info.field('DEC')[i])

          self.R200.append(Halos_info.field('R200')[i])
          self.M200.append(Halos_info.field('M200')[i])
          M500 = Halos_info.field('M200')[i]/1.4
          self.M500.append(M500)
          #normalized mass
          self.nM500.append(M500/(1e14))          

          red_shift = Halos_info.field('Z')[i]
          self.Z_red.append(red_shift)

          self.lgT.append(0.0)
          self.lnMT.append(0.0)
          self.lnML.append(0.0)
          self.lgLx.append(0.0)
          self.lgFx.append(0.0)
          self.lgLxobs.append(0.0)
            
     self.number_of_halos = len(self.Z_red[:])

     self.z_min  = min(self.Z_red[:])
     self.z_max  = max(self.Z_red[:])

     General_Prop.update(self)

     print "Number of Halos = ", self.number_of_halos
     print "HALOS ADDED SUCCESSFULLY."
     raw_input("Press enter to continue ... ")


   def redshift_org(self,Input_Param):
     n = len(self.Z_red[:])
     self.max_Z    = max(self.Z_red[:])

     self.Z_slice  = Input_Param.red_shift_n
     self.Z_group_n= []     
     self.Z_group_halo_counter= zeros([self.Z_slice],dtype=int)     
     
     for i in range(n):
          red_shift = self.Z_red[i]
          for j in range(self.Z_slice):
             if ( (float(j)*self.max_Z/float(self.Z_slice)) < red_shift):
                if (red_shift <= (float(j+1)*self.max_Z/float(self.Z_slice)) ):
                   self.Z_group_halo_counter[j] += 1
                   self.Z_group_n.append(j)      
                   break


   def add_single_data(self,Halos_data,i):
       self.X.append(Halos_data.X[i])
       self.Y.append(Halos_data.Y[i])
       self.Z.append(Halos_data.Z[i])
       self.RA.append(Halos_data.RA[i])
       self.DEC.append(Halos_data.DEC[i])
       self.R200.append(Halos_data.R200[i])
       self.M200.append(Halos_data.R200[i])
       self.M500.append(Halos_data.M500[i])
       self.nM500.append(Halos_data.nM500[i])
       self.Z_red.append(Halos_data.Z_red[i])
       self.lgT.append(Halos_data.lgT[i])
       self.lgLx.append(Halos_data.lgLx[i])
       self.lgFx.append(Halos_data.lgFx[i])
       self.lnMT.append(Halos_data.lnMT[i])
       self.lnML.append(Halos_data.lnML[i])
       self.lgLxobs.append(Halos_data.lgLxobs[i])

   def update_halo_data(self):
       self.number_of_halos = len(self.Z_red[:])
       print "Number of Halos : ", self.number_of_halos
       General_Prop.update(self)



class Z_Sliced_Halo_Object():

   def __init__(self):
     self.X        = []
     self.Y        = []
     self.Z        = []
     self.r2       = []
     self.RA       = []
     self.DEC      = []
     self.M500     = []
     self.M200     = []
     self.R200     = []
     self.nM500    = []
     self.Z_red    = []
     self.lgT      = []
     self.lgLx     = []
     self.lgFx     = []

     self.lnMT = []
     self.lnML = []
     self.lgLxobs = []

     self.z_min    = 0.0
     self.z_max    = 0.0

   def Creat_Halo_data(self,Halos_data,z_group_number):
     self.z_min  = float(z_group_number)/float(Halos_data.Z_slice) * Halos_data.max_Z
     self.z_max  = float(z_group_number+1)/float(Halos_data.Z_slice) * Halos_data.max_Z
     n = len(Halos_data.RA[:])
     for i in range(n):
       if(Halos_data.Z_group_n[i] == z_group_number):
          self.X.append(Halos_data.X[i])
          self.Y.append(Halos_data.Y[i])
          self.Z.append(Halos_data.Z[i])
          self.r2.append(Halos_data.X[i]**2+Halos_data.Y[i]**2+Halos_data.Z[i]**2)
          self.RA.append(Halos_data.RA[i])
          self.DEC.append(Halos_data.DEC[i])
          self.R200.append(Halos_data.R200[i])
          self.M200.append(Halos_data.M200[i])
          self.M500.append(Halos_data.M500[i])
          self.nM500.append(Halos_data.nM500[i])
          self.Z_red.append(Halos_data.Z_red[i])
          self.lgT.append(Halos_data.lgT[i])
          self.lgLx.append(Halos_data.lgLx[i])
          self.lgFx.append(Halos_data.lgFx[i])

          self.lnMT.append(0.0)
          self.lnML.append(0.0)
          self.lgLxobs.append(0.0)

     self.number_of_halos = len(self.Z_red[:])
     print " Halos between z = ", self.z_min , " & z = " , self.z_max , " are created successfully"
     print "Number of Halos : ", self.number_of_halos

