from control.matlab import *
import matplotlib.pyplot as plt
import function_chapt5 as func
import numpy as np
import sympy as sp

g = 9.81  # gravity acceleration[m/s2]
l = 0.2  # arm length[m]
M = 0.5  # arm weight[kg]
mu = 0.015  # viscous friction coeffitient [kg*m^2/s]
J = 0.01  # Inertia [kg*m^2]
ref = 30  # target angle(deg)

# normative model
omega_n = 15
zeta = 0.707
Msys = tf([0, omega_n**2], [1, 2 * zeta * omega_n, omega_n**2])

# model matching
kp = omega_n**2 * J
ki = M * g * l * omega_n / (2 * zeta)
kd = 2 * J * omega_n * zeta + M * g * l / (2 * omega_n * zeta) - mu
Gyr = tf([kp, ki], [J, mu + kd, M * g * l + kp, ki])


yM, tM = step(Msys, np.arange(0, 2, 0.01))
y, t = step(Gyr, np.arange(0, 2, 0.01))

fig, ax = plt.subplots()
ax.plot(tM, yM * ref, label='M', color='k')
ax.plot(t, y * ref, label='Gyr', ls='--', color='k')
func.plot_set(ax, 't', 'y', 'best')
plt.show()
