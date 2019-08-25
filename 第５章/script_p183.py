from control.matlab import *
from control import *
import matplotlib.pyplot as plt
import function_chapt5 as func
import numpy as np
import sympy as sp
from scipy import linalg
import slycot

A = '0 1;-4 5'
B = '0; 1'
C = '1 0'
D = '0'
P = ss(A, B, C, D)

# check controllability
Uc = ctrb(P.A, P.B)
print('Uc=\n', Uc)
print('det(Uc) = ', np.linalg.det(Uc))
print('rank(Uc) = ', np.linalg.matrix_rank(Uc))
