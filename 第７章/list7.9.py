from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import function_chapt7 as func

P = tf([0, 1], [0.5, 1])
print(P)

ts = 0.2  # sampling time

fig, ax = plt.subplots(2, 1)


# digitalizing by 0th order hold
Pd1 = c2d(P, ts, method='zoh')
print('digitalized time system (zoh)', Pd1)
T = np.arange(0, 3, ts)
gain, phase, w = bode(Pd1, np.logspace(-2, 2), Plot=False)
ax[0].semilogx(w, 20 * np.log10(gain), label='zoh')
ax[1].semilogx(w, phase * 180 / np.pi, label='zoh')


# digitalizing by bilinear transform
Pd2 = c2d(P, ts, method='tustin')
print('digitalized time system (tustin)', Pd2)
gain, phase, w = bode(Pd2, np.logspace(-2, 2), Plot=False)
ax[0].semilogx(w, 20 * np.log10(gain), label='tustin')
ax[1].semilogx(w, phase * 180 / np.pi, label='tustin')

# continuous time system
Tc = np.arange(0, 3, 0.01)
Uc = 0.5 * np.sin(6 * Tc) + 0.5 * np.cos(8 * Tc)
gain, phase, w = bode(P, np.logspace(-2, 2), Plot=False)
ax[0].semilogx(w, 20 * np.log10(gain), ls='-.', label='continuous')
ax[1].semilogx(w, phase * 180 / np.pi, ls='-.', label='continuous')

# draw a lin at frequency : omega = pi/ts
ax[0].axvline(np.pi / ts, lw=0.5, c='k')
ax[1].axvline(np.pi / ts, lw=0.5, c='k')
ax[1].legend()
func.bodeplot_set(ax)
plt.show()
