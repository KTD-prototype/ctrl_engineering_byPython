from control.matlab import *
import matplotlib.pyplot as plt
import function_chapt5 as func
import numpy as np
import sympy as sp

s = sp.Symbol('s')
kp, kd, ki = sp.symbols('k_p k_d k_i')
Mgl, mu, J = sp.symbols('Mgl mu J')
sp.init_printing()

G = (kp * s + ki) / (J * s**3 + (mu + kd) * s**2 + (Mgl + kp) * s + ki)
print(sp.series(1 / G, s, 0, 4))
