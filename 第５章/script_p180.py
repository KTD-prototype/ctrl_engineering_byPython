from control.matlab import *
from control import *
import matplotlib.pyplot as plt
import function_chapt5 as func
import numpy as np
import sympy as sp
from scipy import linalg
import slycot

A = '0 1;-4 5'
B = '0;1'
C = '1 0; 0 1'
D = '0;0'
P = ss(A, B, C, D)

Pole = [-1, -1]
F = -acker(P.A, P.B, Pole)
Ac1 = P.A + P.B * F
Pfb = ss(Ac1, P.B, P.C, P.D)  # system that is get stabled by state feedback

Td = np.arange(0, 8, 0.01)
Ud = 0.2 * (Td > 0)  # step disterbance
x, t, _ = lsim(Pfb, Ud, Td, [-0.3, 0.4])

fig, ax = plt.subplots()
ax.plot(t, x[:, 0], label='$x_1$')
ax.plot(t, x[:, 1], ls='-.', label='$x_2$')
func.plot_set(ax, 't', 'x', 'best')
plt.show()
