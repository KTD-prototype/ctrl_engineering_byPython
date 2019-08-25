from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import function_chapt6 as func

beta = 0.1
T2 = 1
K2 = tf([T2, 1], [beta * T2, 1])
gain, phase, w = bode(K2, logspace(-2, 3), Plot=False)
fig, ax = plt.subplots(2, 1)
ax[0].semilogx(w, 20 * np.log10(gain), color='k')
ax[1].semilogx(w, phase * 180 / np.pi, color='k')
func.bodeplot_set(ax)
plt.show()
