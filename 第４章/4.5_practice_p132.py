from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import function as func
import sympy as sp

fig, ax = plt.subplots(2, 1)
LS = func.linestyle_generator()


# 2nd order lag system (with various omega)
P1 = tf([1, 3], [1, 3, 2])
P2 = tf([0, 1], [1, 2, 2, 1])
gain, phase, w = bode(P1, logspace(-2, 2), Plot=False)
pltargs = {'ls': next(LS)}
pltargs['label'] = 'F =' + str(P1)
ax[0].semilogx(w, 20 * np.log10(gain), **pltargs)
ax[1].semilogx(w, phase * 180 / np.pi, **pltargs)

gain, phase, w = bode(P2, logspace(-2, 2), Plot=False)
pltargs = {'ls': next(LS)}
pltargs['label'] = 'F =' + str(P2)
ax[0].semilogx(w, 20 * np.log10(gain), **pltargs)
ax[1].semilogx(w, phase * 180 / np.pi, **pltargs)

func.bodeplot_set(ax, 3, 3)
plt.show()


# for i in range(len(omega_n)):
#     P = tf([0, omega_n[i]**2], [1, 2 * zeta * omega_n[i], omega_n[i]**2])
#     gain, phase, w = bode(P, logspace(-2, 2), Plot=False)
#
#     # plot bode diagram
#     pltargs = {'ls': next(LS)}
#     pltargs['label'] = '$\omega_n$=' + str(omega_n[i])
#     ax[0].semilogx(w, 20 * np.log10(gain), **pltargs)
#     ax[1].semilogx(w, phase * 180 / np.pi, **pltargs)
#
#
# func.bodeplot_set(ax, 3, 3)
# plt.show()
