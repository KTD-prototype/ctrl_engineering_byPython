import control
from control.matlab import *
import sympy as sp


# Practice 2
s = sp.Symbol('s')
extracted_equation = sp.expand((s + 1) * (s + 2)**2, s)
# print(extracted_equation)
Np_2 = [1, 3] # numerator polynominal coefficients of transfer function
Dp_2 = [1, 5, 8, 4] #denominator polynominal coefficients of transfer function
P_2 = tf(Np_2, Dp_2)
print(P_2)

print(P_2.num)
print(P_2.den)

[[numP_2]], [[denP_2]] = tfdata(P_2)
print(numP_2)
print(denP_2)


# Practice 1
Np = [1,2] # numerator polynominal coefficients of transfer function (0*s + 1)
Dp = [1,5,3,4] # denominator polynominal coefficients of transfer function (1*s^2 + 2*s + 3)
P = tf(Np, Dp)
print(P)
