from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import scipy
import function as func

A = [[0, 1], [-4, -5]]
B = [[0], [1]]
C = np.eye(2)  # identity matrix of 2*2
D = np.zeros([2, 1])  # zero matrix of 2*1
P = ss(A, B, C, D)

Td = np.arange(0, 5, 0.01)
Ud = 3 * np.sin(5 * Td)
zero_state = [0, 0]
# X0 = [-0.3, 0.4]
X0 = [0.5, 1]

# xst, t = step(P, Td)  # step response (zero-state response)
xst, t, _ = lsim(P, Ud, Td, zero_state)  # step response (zero-state response)
xin, _ = initial(P, Td, X0)  # zero-input response
x, _, _ = lsim(P, Ud, Td, X0)

fig, ax = plt.subplots(1, 2, figsize=(6, 2.3))
for i in [0, 1]:
    ax[i].plot(t, x[:, i], label='response')
    ax[i].plot(t, xst[:, i], ls='--', label='zero_state')
    ax[i].plot(t, xin[:, i], ls='-.', label='zero_input')

func.plot_set(ax[0], 't', '$x_1$', 'best')
func.plot_set(ax[1], 't', '$x_2$')
fig.tight_layout()
plt.show()
