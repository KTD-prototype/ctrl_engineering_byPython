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

num_delay, den_delay = pade(0.005, 1)  # dead time system
Pdelay = P * tf(num_delay, den_delay)

fig, ax = plt.subplots()

kp0 = 2.9
K = tf([0, kp0], [0, 1])
Gyr = feedback(Pdelay * K, 1)
y, t = step(Gyr, np.arange(0, 2, 0.01))

ax.plot(t, y * ref, color='k')
ax.axhline(ref, color="k", linewidth=0.5)
func.plot_set(ax, 't', 'y')
plt.show()
