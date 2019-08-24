from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import function as func

T, K = 0.5, 1  # set time constant and gain
P = tf([0, K], [T, 1])  # 1st order lag system
y, t = step(P, np.arange(0, 5, 0.01))  # step response

fig, ax = plt.subplots()
ax.plot(t, y)
func.plot_set(ax, 't', 'y')
plt.show()
