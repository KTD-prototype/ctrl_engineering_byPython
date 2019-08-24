import sympy as sp

sp.init_printing()
s = sp.Symbol('s')
T = sp.Symbol('T', real=True)
P = 1 / ((1 + T * s) * s)
aparted_P = sp.apart(P, s)
print(aparted_P)

t = sp.Symbol('t', positive=True)
inv_lap_transformed = sp.inverse_laplace_transform((1 / s) - 1 / (s + 1 / T), s, t)
print(inv_lap_transformed)
