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


# design for state feedback gain to stabilize system P
regulator_poles = [-5 + 5j, -5 - 5j]
F = -acker(P.A, P.B, regulator_poles)

# output feedback (observer + state feedback)
K = ss(P.A + P.B * F + L * P.C, -L, F, 0)
print('K : \n', K)
print('----------------')
print('K(s) = ', tf(K))

# output feedbacked system
Gfb = feedback(P, K, sign=1)

fig, ax = plt.subplots()
Td = np.arange(0, 3, 0.01)

# without output feedback
y, t = initial(P, Td, [-1, 0.5])
ax.plot(t, y, ls='-.', label='w/o controller', color='k')

#  with output feedback
y, t = initial(Gfb, Td, [-1, 0.5, 0, 0])
ax.plot(t, y, label='w/ controller', color='k')

func.plot_set(ax, 't', 'y', 'best')
plt.show()
