from control.matlab import *
import matplotlib.pyplot as plt
import function_chapt5 as func
import numpy as np

g = 9.81  # gravity acceleration[m/s2]
l = 0.2  # arm length[m]
M = 0.5  # arm weight[kg]
mu = 0.015  # viscous friction coeffitient [kg*m^2/s]
J = 0.01  # Inertia [kg*m^2]

kp = [0, 0]
ki = [0, 0]
kd = [0, 0]
Rule = ['', '']
T0 = 0.3
kp0 = 2.9


# limit sensitivity method (classic)
Rule[0] = 'Classic'
kp[0] = 0.6 * kp0
ki[0] = kp[0] / (0.5 * T0)
kd[0] = kp[0] * (0.125 * T0)

# revised limit sensitivity method (no overshoot)
Rule[1] = 'No Overshoot'
kp[1] = 0.2 * kp0
ki[1] = kp[1] / (0.5 * T0)
kd[1] = kp[1] * (0.33 * T0)

LS = func.linestyle_generator()
fig, ax = plt.subplots()

P = tf([0, 1], [J, mu, M * g * l])
ref = 30  # target angle[deg]

num_delay, den_delay = pade(0.005, 1)  # dead time system
Pdelay = P * tf(num_delay, den_delay)


for i in range(2):
    K = tf([kd[i], kp[i], ki[i]], [1, 0])
    Gyr = feedback(Pdelay * K, 1)
    y, t = step(Gyr, np.arange(0, 2, 0.01))

    ax.plot(t, y * ref, ls=next(LS), label=Rule[i])

    print(Rule[i])
    print('kp = ', kp[i])
    print('ki = ', ki[i])
    print('kd = ', kd[i])
    print('--------------')

ax.axhline(ref, color="k", linewidth=0.5)
func.plot_set(ax, 't', 'y')
plt.show()
