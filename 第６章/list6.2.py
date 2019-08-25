from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import function_chapt6 as func

fig, ax = plt.subplots(1, 2)
fig, ax2 = plt.subplots(2, 1)
LS = func.linestyle_generator()


# the case that closed loop system will be unstable
P = tf([0, 1], [1, 1, 1.5, 1])
x, y, _ = nyquist(P, logspace(-3, 5, 1000), Plot=False)
ax[0].plot(x, y, color='k')
ax[0].plot(x, -y, ls='--', color='k')
ax[0].scatter(-1, 0, color='k')
func.plot_set(ax[0], 'Re', 'Im')

gain, phase, w = bode(P, logspace(-2, 2), Plot=False)
pltargs = {'ls': next(LS), 'label': 'P=' + str(P)}
ax2[0].semilogx(w, 20 * np.log10(gain), **pltargs)
ax2[1].semilogx(w, phase * 180 / np.pi, **pltargs)

# the case that closed loop system will be stable
P = tf([0, 1], [1, 2, 2, 1])
x, y, _ = nyquist(P, logspace(-3, 5, 1000), Plot=False)
ax[1].plot(x, y, color='k')
ax[1].plot(x, -y, ls='--', color='k')
ax[1].scatter(-1, 0, color='k')
func.plot_set(ax[1], 'Re', 'Im')

gain, phase, w = bode(P, logspace(-2, 2), Plot=False)
pltargs = {'ls': next(LS), 'label': 'P=' + str(P)}
ax2[0].semilogx(w, 20 * np.log10(gain), **pltargs)
ax2[1].semilogx(w, phase * 180 / np.pi, **pltargs)

fig.tight_layout()
func.bodeplot_set(ax2, 3, 3)
plt.show()
