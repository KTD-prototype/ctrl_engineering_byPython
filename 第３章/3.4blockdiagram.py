import control
from control.matlab import *
import sympy as sp

# serial connection of two systems
S1 = tf([0, 1], [1, 1])
S2 = tf([1, 1], [1, 1, 1])
S = S2 * S1
print('S = ', S)
S = series(S1, S2)
print('S = ', S)

# parallel connection of two systems
S = S1 + S2
print('S = ', S)
S = parallel(S1, S2)
print('S = ', S)

# feedback connection of two systems
S = S1 / (1 + S1 * S2)
print('S = ', S)
print('S = ', S.minreal())
S = feedback(S1, S2)
print('S = ', S)
print('S = ', S.minreal())
