from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import function as func
import sympy as sp

sp.init_printing()
s = sp.Symbol('s')
t = sp.Symbol('t', positive=True)

# fig1, ax1 = plt.subplots()
fig, ax = plt.subplots()
LS = func.linestyle_generator()

omega_n = 2
zeta = 0.5

P1 = tf([0, omega_n**2], [1, 2 * zeta * omega_n, omega_n**2])
P2 = tf([3, omega_n**2], [1, 2 * zeta * omega_n, omega_n**2])
P3 = tf([3, -1 * (omega_n**2)], [1, 2 * zeta * omega_n, omega_n**2])
print(P3)

y, t = step(P1, np.arange(0, 10, 0.01))
ax.plot(t, y, ls=next(LS), label='P1')
y, t = step(P2, np.arange(0, 10, 0.01))
ax.plot(t, y, ls=next(LS), label='P2')
y, t = step(P3, np.arange(0, 10, 0.01))
ax.plot(t, y, ls=next(LS), label='P3')

func.plot_set(ax, 't', 'y', 'best')
plt.show()
