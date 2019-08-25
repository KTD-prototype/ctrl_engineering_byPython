from control.matlab import *
from control import mixsyn
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import function_chapt7 as func

P = tf([0, 1], [0.5, 1])
print(P)

ts = 0.2  # sampling time

# digitalizing by 0th order hold
Pd1 = c2d(P, ts, method='zoh')
print('digitalized time system (zoh)', Pd1)

# digitalizing by bilinear transform
Pd2 = c2d(P, ts, method='tustin')
print('digitalized time system (tustin)', Pd2)
