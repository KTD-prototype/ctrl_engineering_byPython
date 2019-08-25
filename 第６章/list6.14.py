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

fig, ax = plt.subplots()  # for step response
fig, ax1 = plt.subplots(2, 1)  # for bode diagram

# check gain and phase at 40 rad/sec
[[[mag]]], [[[phase]]], omega = freqresp(H1, [40])
magH1at40 = mag
phaseH1at40 = phase * (180 / np.pi)
# compensation of phase lead
# get value to be compensated
phim = (60 - (180 + phaseH1at40)) * np.pi / 180
beta = (1 - np.sin(phim)) / (1 + np.sin(phim))
T2 = 1 / 40 / np.sqrt(beta)
K2 = tf([T2, 1], [beta * T2, 1])
H2 = P * K1 * K2  # open loop system with phase lag+lead complement

# check gain and phase at 40 rad/s
[[[mag2]]], [[[phase2]]], omega2 = freqresp(H2, [40])
magH2at40 = mag2
phaseH2at40 = phase2 * (180 / np.pi)
# compensation of gain
k = 1 / magH2at40  # gain compensation
H3 = P * k * K1 * K2  # open loop system with all types of compensation


# closed loop system after tuning
Gyr_H = feedback(H3, 1)
y, t = step(Gyr_H, np.arange(0, 2, 0.01))
ax.plot(t, y * ref, label='After', color='k')

gain, phase, w = bode(Gyr_H, logspace(-1, 2), Plot=False)
ax1[0].semilogx(w, 20 * np.log10(gain), label='After')
ax1[1].semilogx(w, phase * 180 / np.pi, label='After')


# step response of closed loop system before tuning
Gyr_P = feedback(H0, 1)
y, t = step(Gyr_P, np.arange(0, 2, 0.01))
pltargs = {'ls': '--', 'label': 'Before'}
ax.plot(t, y * ref, **pltargs)

gain, phase, w = bode(Gyr_P, logspace(-1, 2), Plot=False)
ax1[0].semilogx(w, 20 * np.log10(gain), **pltargs)
ax1[1].semilogx(w, phase * 180 / np.pi, **pltargs)


ax.axhline(ref, color="k", linewidth=0.5)
func.plot_set(ax, 't', 'y', 'best')
func.bodeplot_set(ax1)
plt.show()
