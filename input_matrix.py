from sympy import Matrix
from sympy.core.numbers import Rational
from sympy import I #unit imginary number

def frac(a,b):
    return Rational(a)/Rational(b)

A=Matrix([[1,-2,1,-1,3],\
          [2,-4,1,1,2],\
          [1,-2,-2,3,1]])

from frontend import *
from backend import *

step_by_step_output2pdf(find_RREF(A))