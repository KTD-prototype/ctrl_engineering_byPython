from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import function as func
import sympy as sp

fig, ax = plt.subplots(2, 2)

# 2nd order lag system
zeta = 0.7
omega_n = 5
P = tf([0, omega_n**2], [1, 2 * zeta * omega_n, omega_n**2])

freq = [2, 5, 10, 20]  # change freqency of input
Td = np.arange(0, 5, 0.01)
for i in range(2):
    for j in range(2):
        u = np.sin(freq[i + j] * Td)  # sin input
        y, t, X0 = lsim(P, u, Td, 0)

        ax[i, j].plot(t, u, ls='--', label='u')
        ax[i, j].plot(t, y, label='y')
        func.plot_set(ax[i, j], 't', 'u, y')

# func.plot_set(ax[0, 0], 't', 'u, y', 'best')
# func.plot_set(ax[0, 1], 't', 'u, y', 'best')
# func.plot_set(ax[1, 0], 't', 'u, y', 'best')
# func.plot_set(ax[1, 1], 't', 'u, y', 'best')
ax[0, 0].legend()
plt.show()
