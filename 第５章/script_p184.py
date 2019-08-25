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

# check observability
Uo = obsv(A, C)
print('Uo=\n', Uo)
print('det(Uo) = ', np.linalg.det(Uo))
print('rank(Uo) = ', np.linalg.matrix_rank(Uo))
