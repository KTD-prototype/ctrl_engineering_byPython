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

kp = 2
ki = (0, 5, 10)

LS = func.linestyle_generator()
fig, ax = plt.subplots(2, 1)
for i in range(len(ki)):
    K = tf([kp, ki[i]], [1, 0])  # proportional + integral control
    H = P * K  # open loop system
    gain, phase, w = bode(H, logspace(-1, 2), Plot=False)

    # bode diagram
    pltargs = {'ls': next(LS), 'label': '$k_I$=' + str(ki[i])}
    ax[0].semilogx(w, 20 * np.log10(gain), **pltargs)
    ax[1].semilogx(w, phase * 180 / np.pi, **pltargs)

    # gain margin, phase margen, phase cross frequency, gain cross frequency
    print('kI = ', ki[i])
    print('(GM,PM,wpc,wgc)')
    print(margin(H))
    print('--------------------')

func.bodeplot_set(ax, 3)
plt.show()
