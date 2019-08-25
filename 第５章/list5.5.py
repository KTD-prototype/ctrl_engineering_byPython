from control.matlab import *
import matplotlib.pyplot as plt
import function_chapt5 as func
import numpy as np

g = 9.81  # gravity acceleration[m/s2]
l = 0.2  # arm length[m]
M = 0.5  # arm weight[kg]
mu = 0.015  # viscous friction coeffitient [kg*m^2/s]
J = 0.01  # Inertia [kg*m^2]

P = tf([0, 1], [J, mu, M * g * l])
ref = 30  # target angle[deg]

kp = 2
kd = (0, 0.1, 0.2, 1)

LS = func.linestyle_generator()
fig1, ax1 = plt.subplots()

for i in range(len(kd)):
    K = tf([kd[i], kp], [0, 1])  # proportional + defferential control
    Gyr = feedback(P * K, 1)  # closed loop system
    y, t = step(Gyr, np.arange(0, 2, 0.01))  # step response

    pltargs = {'ls': next(LS), 'label': '$k_D$=' + str(kd[i])}
    ax1.plot(t, y * ref, **pltargs)

ax1.axhline(ref, color='k', linewidth=0.5)
func.plot_set(ax1, 't', 'y', 'best')


fig, ax2 = plt.subplots(2, 1)
for i in range(len(kd)):
    K = tf([kd[i], kp], [0, 1])  # proportional control
    Gyr = feedback(P * K, 1)  # closed loop system
    gain, phase, w = bode(Gyr, logspace(-1, 2), Plot=False)  # bode diagram

    pltargs = {'ls': next(LS), 'label': '$k_D$=' + str(kd[i])}
    ax2[0].semilogx(w, 20 * np.log10(gain), **pltargs)
    ax2[1].semilogx(w, phase * 180 / np.pi, **pltargs)

func.bodeplot_set(ax2, 'lower left')

plt.show()
