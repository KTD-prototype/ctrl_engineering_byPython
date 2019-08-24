from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import scipy
import function as func

P1 = tf([0, 1], [1, 1])
print('P1:', pole(P1))

P2 = tf([0, 1], [-1, 1])
print('P2:', pole(P2))

P3 = tf([0, 1], [1, 0.05, 1])
print('P3:', pole(P3))

P4 = tf([0, 1], [1, -0.05, 1])
print('P4:', pole(P4))

[[Np]], [[Dp]] = tfdata(P4)
print(Dp)
print(np.roots(Dp))
