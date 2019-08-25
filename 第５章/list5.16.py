from control.matlab import *
import matplotlib.pyplot as plt
import function_chapt5 as func
import numpy as np
import sympy as sp

A = '0 1;-4 5'
B = '0;1'
C = '1 0; 0 1'
D = '0;0'
P = ss(A, B, C, D)

Pole = [-1, -1]
F = -acker(P.A, P.B, Pole)
print(F)

print(np.linalg.eigvals(P.A + P.B * F))

Ac1 = P.A + P.B * F
Pfb = ss(Ac1, P.B, P.C, P.D)

Td = np.arange(0, 5, 0.01)
X0 = [-0.3, 0.4]
x, t = initial(Pfb, Td, X0)

fig, ax = plt.subplots()
ax.plot(t, x[:, 0], label='$x_1$')
ax.plot(t, x[:, 1], ls='-.', label='$x_2$')
func.plot_set(ax, 't', 'x', 'best')
plt.show()
