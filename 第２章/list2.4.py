from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# define differential equation


def system(y, t):
    if t < 10.0:
        u = 0.0
    else:
        u = 1.0

    dydt = (- y + u) / 5.0
    return dydt


# set initial value and time, and solve the differential equation
y0 = 0.5
t = np.arange(0, 40, 0.04)
y = odeint(system, y0, t)

# draw a graph
fig, ax = plt.subplots()  # generate an object of figure and axes
ax.plot(t, y, label='y')  # generate a graph in the axes object
ax.plot(t, 1 * (t >= 10), ls='--', label='u')
ax.set_xlabel('t')
ax.set_ylabel('y, u')
ax.legend(loc='best')
ax.grid(ls=':')

plt.show()
