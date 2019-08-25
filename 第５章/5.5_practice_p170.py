from control.matlab import *
import matplotlib.pyplot as plt
import function_chapt5 as func
import numpy as np
import sympy as sp

s = sp.Symbol('s')
kp, kd, ki = sp.symbols('k_p k_d k_i')
Mgl, mu, J = sp.symbols('Mgl mu J')
alpha1, alpha2 = sp.symbols('alpha_1 alpha_2')
z, wn = sp.symbols('zeta omega_n')
sp.init_printing()

G = ki / (J * s**3 + (mu + kd) * s**2 + (Mgl + kp) * s + ki)
M = wn**3 / (s**3 + alpha2 * wn * s**2 + alpha1 * s * wn**2 + wn**3)
print(sp.series(1 / G, s, 0, 4))
# ans = J*s**3/k_i + s**2*(k_d/k_i + mu/k_i) + s*(Mgl/k_i + k_p/k_i) + 1
print(sp.series(1 / M, s, 0, 4))
# ans = alpha_1*s/omega_n + alpha_2*s**2/omega_n**2 + 1 + s**3/omega_n**3

f1 = Mgl / ki + kp / ki - alpha1 / wn
f2 = kd / ki + mu / ki - alpha2 / (wn**2)
f3 = J / ki - 1 / (wn**3)

print(sp.solve([f1, f2, f3], [kp, ki, kd]))
# ans = {k_p: J*alpha_1*omega_n**2 - Mgl, k_i: J*omega_n**3, k_d: J*alpha_2*omega_n - mu}
