from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import function as func

fig, ax = plt.subplots()
LS = func.linestyle_generator()

# zeta = [1, 0.7, 0.4]
zeta = [0.1, 0, -0.05]
omega_n = 5

# zeta, omega_n = 0.4, 5 #setting dumping coefficient and singular angular frequency

# step response of second order lag system
for i in range(len(zeta)):
    P = tf([0, omega_n**2], [1, 2 * zeta[i] * omega_n, omega_n**2])
    y, t = step(P, np.arange(0, 5, 0.01))

    pltargs = {'ls': next(LS)}
    pltargs['label'] = '$\zeta$ = ' + str(zeta[i])
    ax.plot(t, y, **pltargs)

func.plot_set(ax, 't', 'y', 'best')
