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
kd = 0.1
ki = 10

K1 = tf([kd, kp, ki], [1, 0])
K2 = tf([kp, ki], [kd, kp, ki])
K3 = tf([0, ki], [kd, kp, ki])

# transfer function from z to y
Gyz = feedback(P * K1, 1)

Td = np.arange(0, 2, 0.01)
r = 1 * (Td > 0)

# form target:r by K2
z, t, _ = lsim(K2, r, Td, 0)
# form target:r by K3
z2, t, _ = lsim(K3, r, Td, 0)

# transfer function from (formed) target z(r) to u
K1p = feedback(K1, P)

fig, ax = plt.subplots(1, 3)

# PID control(suppose z = r)
y, _, _ = lsim(Gyz, r, Td, 0)
# y, _, _ = lsim(K1p, r, Td, 0)
ax[0].plot(t, r * ref, color='k')
ax[1].plot(t, y * ref, ls='--', label='PID', color='k')
# ax[2].plot(t, u * ref, ls='--', label='PID', color='k')

# PI-D control
y, _, _ = lsim(Gyz, z, Td, 0)
ax[0].plot(t, z * ref, color='k')
ax[1].plot(t, y * ref, label='PI-D', color='k')
# ax[2].plot(t, u2 * ref, ls='--', label='PI-D', color='k')

# I-PD control
y, _, _ = lsim(Gyz, z2, Td, 0)
ax[0].plot(t, z2 * ref, color='k')
ax[1].plot(t, y * ref, ls=':', label='I-PD', color='k')
# ax[2].plot(t, u3 * ref, ls='--', label='I-PD', color='k')


ax[1].axhline(ref, color='k', linewidth=0.5)
func.plot_set(ax[0], 't', 'r')
func.plot_set(ax[1], 't', 'r', 'best')
# func.plot_set(ax[2], 't', 'r', 'best')
plt.show()
