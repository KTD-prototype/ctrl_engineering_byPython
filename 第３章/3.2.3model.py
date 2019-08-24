import control
from control.matlab import *

# numerator polynominal coefficients of transfer function (0*s + 1)
Np = [0, 1]
# denominator polynominal coefficients of transfer function (1*s^2 + 2*s + 3)
Dp = [1, 2, 3]
P = tf(Np, Dp)
print(P)

P2 = tf([0, 1], [1, 2, 3])  # other way to express transfer function
print(P2)
