from sympy import Matrix
from sympy.core.numbers import Rational
from sympy import I #unit imginary number

def frac(a,b):
    return Rational(a)/Rational(b)

A=Matrix([[1,-2,1,-1,3],\
          [2,-4,1,1,2],\
          [1,-2,-2,3,1]])
# A=Matrix([[-1,1,1,-1],\
#          [1,-2,2,-1]])
# A=Matrix([[2,-4,3,0,1,6],\
#          [1,-2,-2,14,-4,15],\
#          [1,-2,1,2,1,-1],\
#          [-2,4,0,-12,1,-7]])
# A=Matrix([[1,2,1,1,0,0],\
#          [2,-1,5,0,1,0],\
#          [-1,3,0,0,0,1]])
# A=Matrix([[-2,1,3,-5,4],\
#          [-1,0,3,-4,4],\
#          [-1,-1,6,-6,7]])
# A=Matrix([[2,-1,1,3,0],\
#          [1,-1,2,1,1],\
#          [1,1,3,3,-3]])
# A=Matrix([[1,1,1,1,0,0],\
#          [1,-1,1,0,1,0],\
#          [4,2,1,0,0,1]])
A=Matrix([[-2,1,1,0],\
          [frac(3,2),-frac(1,2),0,1]])
# A=Matrix([[1,2,1,0],\
#           [3,4,0,1]])
# A=Matrix([[0,-I,1,0],\
#           [I, 0,0,1]])
# A=Matrix([[1,-2-2*I,1,0],\
#           [2-2*I, 1,0,1]])
# A=frac(1,9)*Matrix([[1,2+2*I,9,0],\
#                     [-2+2*I, 1,0,9]])

from frontend import *
from backend import *

step_by_step_output2pdf(find_RREF(A))