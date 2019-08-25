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

kp = (0.5, 1, 2, 10)

LS = func.linestyle_generator()
fig1, ax1 = plt.subplots()

for i in range(len(kp)):
    K = tf([0, kp[i]], [0, 1])  # proportional control
    Gyr = feedback(P * K, 1)  # closed loop system
    y, t = step(Gyr, np.arange(0, 2, 0.01))  # step response

    pltargs = {'ls': next(LS), 'label': '$k_P$=' + str(kp[i])}
    ax1.plot(t, y * ref, **pltargs)

ax1.axhline(ref, color='k', linewidth=0.5)
func.plot_set(ax1, 't', 'y', 'best')
plt.show()
