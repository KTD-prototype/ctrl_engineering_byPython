from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import function_chapt6 as func

# P = tf([0, 1], [1, 1, 1.5, 1])
P = tf([0, 1], [1, 2, 2, 1])
# get a frequency when the phase will delay for 180 deg
_, _, wpc, _ = margin(P)

t = np.arange(0, 30, 0.1)
u = np.sin(wpc * t)
y = 0 * u

fig, ax = plt.subplots(2, 2)
for i in range(2):
    for j in range(2):
        # feedback the output negatively, and generate new input at next time stamp
        u = np.sin(wpc * t) - y
        y, t, x0 = lsim(P, u, t, 0)

        ax[i, j].plot(t, u, ls='--', label='u')
        ax[i, j].plot(t, y, label='y')
        func.plot_set(ax[i, j], 't', 'u, y')

fig.tight_layout()
plt.show()
