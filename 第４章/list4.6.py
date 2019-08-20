from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import function as func

fig, ax = plt.subplots()
LS = func.linestyle_generator()

K = [1, 2, 3]
T = 0.5
# T = (1, 0.5, 0.1)
# T = -1

for i in range(len(K)):
    y, t = step(tf([0, K[i]], [T, 1]), np.arange(0, 5, 0.01))
    ax.plot(t, y, ls = next(LS), label = 'K = ' + str(K[i]))

func.plot_set(ax, 't', 'y', 'upper left')



# T, K = 0.5, 1 #set time constant and gain
# P = tf([0, K], [T, 1]) # 1st order lag system
# y, t = step(P, np.arange(0, 5, 0.01)) # step response
