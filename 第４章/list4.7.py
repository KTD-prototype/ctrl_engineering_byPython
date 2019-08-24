from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import function as func

fig, ax = plt.subplots()

zeta, omega_n = 0.4, 5  # setting dumping coefficient and singular angular frequency

# step response of second order lag system
P = tf([0, omega_n**2], [1, 2 * zeta * omega_n, omega_n**2])
y, t = step(P, np.arange(0, 5, 0.01))

ax.plot(t, y)
func.plot_set(ax, 't', 'y')
plt.show()
