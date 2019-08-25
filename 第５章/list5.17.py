from control.matlab import *
from control import *
import matplotlib.pyplot as plt
import function_chapt5 as func
import numpy as np
import sympy as sp
from scipy import linalg
import slycot

A = '0 1;-4 5'
B = '0;1'
C = '1 0; 0 1'
D = '0;0'
P = ss(A, B, C, D)

Q = [[100, 0], [0, 1]]
R = 1
F, X, E = lqr(P.A, P.B, Q, R)
# X, E, F = care(P.A, P.B, Q, R)
F = -F

H1 = np.c_[P.A, -P.B * (1 / R) * P.B.T]
H2 = np.c_[Q, P.A.T]
H = np.r_[H1, -H2]
eigH = np.linalg.eigvals(H)
print(eigH)

print('---stable eigen values of Hamilton matrix---')
eigH_stable = [i for i in eigH if i < 0]  # extract eigen value with negative real part
print(eigH_stable)

F = -acker(P.A, P.B, eigH_stable)
print('---feedback gain---')
print(F)
