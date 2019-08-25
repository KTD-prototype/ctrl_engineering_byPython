from control.matlab import *
import matplotlib.pyplot as plt
import function_chapt5 as func
import numpy as np
import sympy as sp

s = sp.Symbol('s')
z, wn = sp.symbols('zeta omega_n')
kp, kd, ki = sp.symbols('k_p k_d k_i')
Mgl, mu, J = sp.symbols('Mgl mu J')
sp.init_printing()

f1 = Mgl / ki - 2 * z / wn
f2 = (mu + kd) / ki - Mgl * kp / (ki**2) - 1 / (wn**2)
f3 = J / ki - kp * (mu + kd) / (ki**2) + Mgl * kp**2 / (ki**3)

print(sp.solve([f1, f2, f3], [kp, ki, kd]))
