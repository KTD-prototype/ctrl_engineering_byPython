from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import scipy
import function as func

w = 1.5  # setting for step size
Y, X = np.mgrid[-w:w:100j, -w:w:100j]

A = np.array([[0, 1], [-4, -5]])
s, v = np.linalg.eig(A)  # eigen vector v and eigen value s for matrix A

# calculate components of \dot{x} by using \dot{x} = Ax
U = A[0, 0] * X + A[0, 1] * Y
V = A[1, 0] * X + A[1, 1] * Y

t = np.arange(-1.5, 1.5, 0.01)

fig, ax = plt.subplots()

# plot invariant set only when eigen value of A is a real number
if s.imag[0] == 0 and s.imag[1] == 0:
    ax.plot(t, (v[1, 0] / v[0, 0]) * t, ls='-')
    ax.plot(t, (v[1, 1] / v[0, 1]) * t, ls='-')

# plot phase plane diagram for x
ax.streamplot(X, Y, U, V, density=0.7, color='k')
func.plot_set(ax, '$x_1$', '$x_2$')
plt.show()
