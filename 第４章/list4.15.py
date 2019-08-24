from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import function as func
import sympy as sp

fig, ax = plt.subplots(2, 1)
LS = func.linestyle_generator()

# 1st order lag system
K = 1
T = [1, 0.5, 0.1]

for i in range(len(T)):
    P = tf([0, K], [T[i], 1])
    gain, phase, w = bode(P, logspace(-2, 2), Plot=False)

    # plot bode diagram
    pltargs = {'ls': next(LS), 'label': 'T = ' + str(T[i])}
    ax[0].semilogx(w, 20 * np.log10(gain), **pltargs)
    ax[1].semilogx(w, phase * 180 / np.pi, **pltargs)

func.bodeplot_set(ax, 3, 3)
plt.show()
