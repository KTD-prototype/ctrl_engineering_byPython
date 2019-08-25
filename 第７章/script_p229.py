from control.matlab import *
from control import *
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from scipy import linalg
import slycot

A = '0 1;-4 5'
B = '0; 1'
C = '1 0'
D = '0'
P = ss(A, B, C, D)

# observer pole
observer_poles = [-15 + 5j, -15 - 5j]

# design for observer gains [correspondents to state feedbacks]
L = -acker(P.A.T, P.C.T, observer_poles).T

print(L)
print(np.linalg.eigvals(P.A + L * P.C))
