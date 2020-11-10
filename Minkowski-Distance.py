from math import *
from decimal import Decimal 

class Solver:
   #Minkowski distance formula function
   def minkowski_distance(x, y, p_value):  
      return (p_root(sum(pow(abs(a-b), p_value) 
               for a, b in zip(x, y)), p_value)) 

#Function to get distance between two points and calculate distance value to given
#Which is then passed to the minkowski distance function
def p_root(value, root): 
      root_value = 1 / float(root) 
      return round (Decimal(value) **
               Decimal(root_value), 3)

x = [5] 
y = [8] 
q = 3


print(Solver.minkowski_distance(x, y, q)) 

### Attributions to my code
### I retrieved the Minkowski Distance Formula from https://www.geeksforgeeks.org/
