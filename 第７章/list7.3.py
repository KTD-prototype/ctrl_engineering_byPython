from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import function_chapt7 as func

g = 9.81  # gravity acceleration[m/s2]
l = 0.2  # arm length[m]
M = 0.5  # arm weight[kg]
mu = 0.015  # viscous friction coeffitient [kg*m^2/s]
J = 0.01  # Inertia [kg*m^2]

Pn = tf([0, 1], [J, mu, M * g * l])

# uncertainty
delta = np.arange(-1, 1, 0.1)
WT = tf([10, 0], [1, 150])

fig, ax = plt.subplots(1, 2)

for i in range(len(delta)):
    # control target with uncertainty
    P = (1 + WT * delta[i]) * Pn
    gain, _, w = bode(P, logspace(-3, 3), Plot=False)
    ax[0].semilogx(w, 20 * np.log10(gain), color='k', lw=0.3)

    # productive uncertainty
    DT = (P - Pn) / Pn
    gain, _, w = bode(DT, logspace(-3, 3), Plot=False)
    ax[1].semilogx(w, 20 * np.log10(gain), color='k', lw=0.3)

gain, phase, w = bode(Pn, logspace(-3, 3), Plot=False)
ax[0].semilogx(w, 20 * np.log10(gain), color='k', lw=2)

gain, phase, w = bode(WT, logspace(-3, 3), Plot=False)
ax[1].semilogx(w, 20 * np.log10(gain), color='k', lw=2)

func.bodeplot_set(ax)
ax[0].set_xlabel('$\omega$ [rad/s]')
ax[0].set_ylabel('Gain of $P$ [dB]')
ax[1].set_ylabel('Gain of $\Delta W_T/P$ [dB]')

plt.show()
