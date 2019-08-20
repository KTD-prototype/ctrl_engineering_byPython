import control
from control.matlab import *
import sympy as sp

# definition of each subsystem
S1 = tf([0, 1], [1, 1])
S2 = tf([0, 1], [1, 2])
S3 = tf([3, 1], [1, 0])
S4 = tf([2, 0], [0, 1])

# caluculate total system S
S12 = feedback(S1, S2)
S123 = series(S12, S3)
S = feedback(S123, S4)
print('S = ', S)
