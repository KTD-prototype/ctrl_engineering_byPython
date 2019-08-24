from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import scipy
import function as func

sp.init_printing()
s = sp.Symbol('s')
t = sp.Symbol('t', positive=True)

A = np.array([[0, 1], [-4, -5]])

# calculation to get matrix-exponential(using inverse laplace transform)
G = s * sp.eye(2) - A
exp_At_1 = sp.inverse_laplace_transform(sp.simplify(G.inv()), s, t)
print(exp_At_1)

# show matrix-exponential at a certain time point
t_1 = 5
print(scipy.linalg.expm(A * t_1))
