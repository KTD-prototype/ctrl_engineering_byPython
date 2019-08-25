from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import function_chapt6 as func

g = 9.81  # gravity acceleration[m/s2]
l = 0.2  # arm length[m]
M = 0.5  # arm weight[kg]
mu = 0.015  # viscous friction coeffitient [kg*m^2/s]
J = 0.01  # Inertia [kg*m^2]

P = tf([0, 1], [J, mu, M * g * l])
ref = 30  # target angle[deg]

# compensation of phase lag
alpha = 20
T1 = 0.25
K1 = tf([alpha * T1, alpha], [alpha * T1, 1])
print('K1 = ', K1)

H0 = P  # base open loop system
H1 = P * K1  # open loop system with phase lag complement

gain0, phase0, w0 = bode(H0, logspace(-1, 2), Plot=False)
gain1, phase1, w1 = bode(H1, logspace(-1, 2), Plot=False)

fig, ax0 = plt.subplots(2, 1)
fig, ax1 = plt.subplots(2, 1)

ax0[0].semilogx(w0, 20 * np.log10(gain0), color='k')
ax0[1].semilogx(w0, phase0 * 180 / np.pi, color='k')

ax1[0].semilogx(w1, 20 * np.log10(gain1), color='b')
ax1[1].semilogx(w1, phase1 * 180 / np.pi, color='b')
func.bodeplot_set(ax0)
func.bodeplot_set(ax1)

# check gain and phase at 40 rad/sec
[[[mag]]], [[[phase]]], omega = freqresp(H1, [40])
magH1at40 = mag
phaseH1at40 = phase * (180 / np.pi)
print('------------------')
print('gain at 40 rad/s = ', 20 * np.log10(magH1at40))
print('phase at 40 rad/s = ', phaseH1at40)


# compensation of phase lead
# get value to be compensated
phim = (60 - (180 + phaseH1at40)) * np.pi / 180
beta = (1 - np.sin(phim)) / (1 + np.sin(phim))

T2 = 1 / 40 / np.sqrt(beta)
K2 = tf([T2, 1], [beta * T2, 1])
print('K2 = ', K2)

fig, ax2 = plt.subplots(2, 1)
H2 = P * K1 * K2  # open loop system with phase lag+lead complement
gain2, phase2, w2 = bode(H2, logspace(-1, 2), Plot=False)
ax2[0].semilogx(w2, 20 * np.log10(gain2), color='r')
ax2[1].semilogx(w2, phase2 * 180 / np.pi, color='r')
func.bodeplot_set(ax2)

# check gain and phase at 40 rad/s
[[[mag2]]], [[[phase2]]], omega2 = freqresp(H2, [40])
magH2at40 = mag2
phaseH2at40 = phase2 * (180 / np.pi)
print('------------------')
print('gain at 40 rad/s = ', 20 * np.log10(magH2at40))
print('phase at 40 rad/s = ', phaseH2at40)


plt.show()
