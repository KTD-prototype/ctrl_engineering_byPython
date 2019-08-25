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

print('---feedback gain---')
print(F)
print(-(1 / R) * P.B.T * X)
print('---pole for closed loop---')
print(E)
print(np.linalg.eigvals(P.A + P.B * F))
