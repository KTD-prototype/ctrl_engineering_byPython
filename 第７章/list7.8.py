from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import function_chapt7 as func

P = tf([0, 1], [0.5, 1])
print(P)

ts = 0.2  # sampling time

fig, ax = plt.subplots(1, 2)


# digitalizing by 0th order hold
Pd1 = c2d(P, ts, method='zoh')
print('digitalized time system (zoh)', Pd1)
T = np.arange(0, 3, ts)
U = 0.5 * np.sin(6 * T) + 0.5 * np.cos(8 * T)
y, t, x0 = lsim(Pd1, U, T)
ax[0].plot(t, y, ls='', marker='o', label='zoh')

# digitalizing by bilinear transform
Pd2 = c2d(P, ts, method='tustin')
print('digitalized time system (tustin)', Pd2)
T = np.arange(0, 3, ts)
y, t, x0 = lsim(Pd2, U, T)
ax[1].plot(t, y, ls='', marker='o', label='tustin')

# continuous time system
Tc = np.arange(0, 3, 0.01)
Uc = 0.5 * np.sin(6 * Tc) + 0.5 * np.cos(8 * Tc)
y, t, x0 = lsim(P, Uc, Tc)
ax[0].plot(t, y, ls='-.')
ax[1].plot(t, y, ls='-.')

func.plot_set(ax[0], 't', 'y', 'best')
func.plot_set(ax[1], 't', 'y', 'best')
plt.show()
