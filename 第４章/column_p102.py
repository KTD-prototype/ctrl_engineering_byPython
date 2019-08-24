import sympy as sp

sp.init_printing()
s = sp.Symbol('s')
t = sp.Symbol('t', positive=True)
w = sp.Symbol('w', real=True)
# P = sp.apart(w**2 / s / (s + w)**2, s)
# print(sp.inverse_laplace_transform(P, s, t))

p1 = sp.Symbol('p1', real=True)
p2 = sp.Symbol('p2', real=True)
P = sp.apart(w**2 / (s * (s - p1) * (s - p2)), s)
print(sp.inverse_laplace_transform(P, s, t))
