from control.matlab import *
from control import *
import matplotlib.pyplot as plt
import function_chapt5 as func
import numpy as np
import sympy as sp
from scipy import linalg
import slycot

A = '0 1;-4 5'
B = '0; 1'
C = '1 0'
D = '0'
P = ss(A, B, C, D)

# extended system
Ae1 = np.c_[P.A, np.zeros((2, 1))]
Ae = np.r_[Ae1, -np.c_[P.C, 0]]
Be = np.c_[P.B.T, 0].T
Ce = np.c_[P.C, 0]

# state feedback control to extended system
Pole = [-1, -1, -5]
Fe = -acker(Ae, Be, Pole)

# closed loop system
Ac1 = Ae + Be * Fe
Pfb = ss(Ac1, Be, np.eye(3), np.zeros((3, 1)))

Td = np.arange(0, 8, 0.01)
Ud = 0.2 * (Td > 0)  # step disterbance
x, t, _ = lsim(Pfb, Ud, Td, [-0.3, 0.4, 0])

fig, ax = plt.subplots()
ax.plot(t, x[:, 0], label='$x_1$')
ax.plot(t, x[:, 1], ls='-.', label='$x_2$')
func.plot_set(ax, 't', 'x', 'best')
plt.show()
