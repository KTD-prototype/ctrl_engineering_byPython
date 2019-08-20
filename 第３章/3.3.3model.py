import control
from control.matlab import *
import sympy as sp

A = '0 1; -1 -1'
B = '0; 1'
C = '1 0'
D = '0'
P = ss(A, B, C, D)
print(P)

A1 = '1 1 2; 2 1 1; 3 4 5'
B1 = '2; 0; 1'
C1 = '1 1 0'
D1 = '1'
P1 = ss(A1, B1, C1, D1)
print(P1)

print('A1 = ', P1.A)
print('B1 = ', P1.B)
print('C1 = ', P1.C)
print('D1 = ', P1.D)

sysA, sysB, sysC, sysD = ssdata(P1)
print(sysA)
print(sysB)
print(sysC)
print(sysD)
