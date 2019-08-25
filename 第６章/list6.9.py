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

kp = (2, 1)
ki = (5, 0)
kd = (0.1, 0)
Label = ('After', 'Before')
Label2 = ('closed_After', 'closed_Before')

LS = func.linestyle_generator()
LS2 = func.linestyle_generator()
LS3 = func.linestyle_generator()
fig, ax = plt.subplots(2, 1)
fig, ax2 = plt.subplots()
fig, ax3 = plt.subplots(2, 1)

for i in range(2):
    K = tf([kd[i], kp[i], ki[i]], [1, 0])  # proportional + integral control
    H = P * K  # open loop system
    gain, phase, w = bode(H, logspace(-1, 2), Plot=False)

    # closed loop system (step response)
    Gyr = feedback(P * K, 1)
    y, t = step(Gyr, np.arange(0, 2, 0.01))
    pltargs2 = {'ls': next(LS2), 'label': Label2[i]}
    ax2.plot(t, y * ref, **pltargs2)

    # closed loop system (bode diagram
    gain, phase, w = bode(Gyr, logspace(-1, 2), Plot=False)
    pltargs3 = {'ls': next(LS2), 'label': Label2[i]}
    ax3[0].semilogx(w, 20 * np.log10(gain), **pltargs3)
    ax3[1].semilogx(w, phase * 180 / np.pi, **pltargs3)

    # bode diagram
    pltargs = {'ls': next(LS), 'label': Label[i]}
    ax[0].semilogx(w, 20 * np.log10(gain), **pltargs)
    ax[1].semilogx(w, phase * 180 / np.pi, **pltargs)

    # gain margin, phase margen, phase cross frequency, gain cross frequency
    print('kP = ', kp[i], 'kI = ', ki[i], 'kD = ', kd[i])
    print('(GM,PM,wpc,wgc)')
    print(margin(H))
    print('--------------------')

func.bodeplot_set(ax, 3)
func.bodeplot_set(ax3, 3)
ax2.axhline(ref, color="k", linewidth=0.5)
func.plot_set(ax2, 't', 'y', 'best')
plt.show()
