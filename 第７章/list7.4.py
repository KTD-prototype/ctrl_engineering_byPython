from control.matlab import *
from control import mixsyn
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

WS = tf([0, 1], [1, 1, 0.25])  # weighting function to sensitivity function
WU = tf(1, 1)
WT = tf([10, 0], [1, 150])  # seighting function to complementary sensitivity function

# mixed sensitivity problem
K, _, gamma = mixsyn(Pn, w1=WS, w2=WU, w3=WT)
print('K = ', ss2tf(K))
print('gamma = ', gamma[0])

fig, ax = plt.subplots(1, 2)

# sensitivity function
Ssys = feedback(1, Pn * K)
gain, _, w = bode(Ssys, logspace(-3, 3), Plot=False)
ax[0].semilogx(w, 20 * np.log10(gain), ls='-', lw=2, label='$S$')
gain, _, w = bode(1 / WS, logspace(-3, 3), Plot=False)
ax[0].semilogx(w, 20 * np.log10(gain), ls='-.', label='$1/W_S$')

# complementary sensitivity function
Tsys = feedback(Pn * K, 1)
gain, _, w = bode(Tsys, logspace(-3, 3), Plot=False)
ax[1].semilogx(w, 20 * np.log10(gain), ls='-', lw=2, label='$T$')
gain, _, w = bode(1 / WT, logspace(-3, 3), Plot=False)
ax[1].semilogx(w, 20 * np.log10(gain), ls='--', label='$1/W_T$')

for i in range(2):
    ax[i].set_ylim(-40, 40)
    ax[i].legend()
    ax[i].grid(which="both", ls=':')
    ax[i].set_ylabel('Gain [dB]')
    ax[i].set_xlabel('$\omega$ [rad/s]')


fig.tight_layout()
plt.show()
