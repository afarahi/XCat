# -- make normal deviates (g)
def normal_dev(n):
   from random import random
   from numpy  import zeros, sqrt, log
   gdev   = zeros(n)
   gdevx  = zeros(n)
   i      = 0
   while (i<n):
      v1 = random()
      v2 = random()
      r  = v1**2 + v2**2
      if (r < 1.0 and r > 0.0):
        fac      = sqrt(-2.0*log(r)/r)
        gdev[i]  = v1*fac
        gdevx[i] = v2*fac
        i       += 1
   return (gdev,gdevx)

