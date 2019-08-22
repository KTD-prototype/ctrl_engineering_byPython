from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import function as func
import sympy as sp

sp.init_printing()
s = sp.Symbol('s')
t = sp.Symbol('t', positive = True)

# fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
LS = func.linestyle_generator()

P1 = sp.expand(((s + 3) / ((s + 1)*(s + 2))), s)
P1 = tf([1, 3], [1, 3, 2])
P2 = tf([0, 1], [1, 2, 2, 1])
# print(P2)

y1, t = step(P1, np.arange(0, 10, 0.01))
y2, t = step(P2, np.arange(0, 10, 0.01))

# ax1.plot(t, y1)
ax2.plot(t, y2)
# func.plot_set(ax1, 't', 'y1')
func.plot_set(ax2, 't', 'y2')
