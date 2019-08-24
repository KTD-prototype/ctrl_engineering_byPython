from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import function as func

A = [[0, 1], [-4, -5]]
B = [[0], [1]]
C = np.eye(2)  # identity matrix of 2*2
D = np.zeros([2, 1])  # zero matrix of 2*1
P = ss(A, B, C, D)
# print(P)

Td = np.arange(0, 5, 0.01)
X0 = [-0.3, 0.4]
x, t = initial(P, Td, X0)  # response to initial value (with zero input)
fig, ax = plt.subplots()
ax.plot(t, x[:, 0], label='$x_1$')
ax.plot(t, x[:, 1], label='$x_2$')
func.plot_set(ax, 't', 'x', 'best')
plt.show()
