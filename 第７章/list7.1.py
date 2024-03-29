from control.matlab import *
from control import *
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from scipy import linalg
import slycot
import function_chapt7 as func

A = '0 1;-4 5'
B = '0; 1'
C = '1 0'
D = '0'
P = ss(A, B, C, D)

# observer pole
observer_poles = [-15 + 5j, -15 - 5j]
# design for observer gains [correspondents to state feedbacks]
L = -acker(P.A.T, P.C.T, observer_poles).T

fig, ax = plt.subplots(1, 2)
Td = np.arange(0, 3, 0.01)
X0 = [-1, 0.5]

# design for state feedback gain to stabilize system P
regulator_poles = [-5 + 5j, -5 - 5j]
F = -acker(P.A, P.B, regulator_poles)

# true behavior of the state
Gsf = ss(P.A + P.B * F, P.B, np.eye(2), [[0], [0]])
x, t = initial(Gsf, Td, X0)
ax[0].plot(t, x[:, 0], ls='-.', label='${x}_1$')
ax[1].plot(t, x[:, 1], ls='-.', label='${x}_2$')

# behaviour that is estimated by observer
# input : u = F * x
u = [[F[0, 0] * x[i, 0] + F[0, 1] * x[i, 1]] for i in range(len(x))]

# output :y = C * x
y = x[:, 0]

# state estimation by observer
Obs = ss(P.A + L * P.C, np.c_[P.B, -L], np.eye(2), [[0, 0], [0, 0]])
xhat, t, x0 = lsim(Obs, np.c_[u, y], Td, [0, 0])
ax[0].plot(t, xhat[:, 0], label='$\hat{x}_1$')
ax[1].plot(t, xhat[:, 1], label='$\hat{x}_2$')

for i in [0, 1]:
    func.plot_set(ax[i], 't', '', 'best')
ax[0].set_ylabel('$x_1, \hat{x}_1$')
ax[1].set_ylabel('$x_2, \hat{x}_2$')
fig.tight_layout()
plt.show()
