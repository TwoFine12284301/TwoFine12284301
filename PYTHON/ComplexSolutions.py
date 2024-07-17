#!/usr/bin/env python3 

from math import pi
from fractions import Fraction

def solutions():
 k_list = [0, 1, 2, 3, 4, 6]
 k_result = []
 base = 5.2073231
 base2 = 10.50064016


#for k in k_list:
# result = (base + (2*k)*pi)
# if 0 <= result < 2*pi:
#    if result == -0.88:
#       k_result.append(result)

#for k in k_list:
# result = (base2 + (2*k)*pi)
# if 0 <= result < 2*pi:
#   if result == 0.88:
#     k_result.append(result)


 for k in k_list:
  result = (base + k*pi)
  k_result.append(Fraction(result))

 return(k_result)
  
