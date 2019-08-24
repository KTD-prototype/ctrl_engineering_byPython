import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 1)  # arrange graphs in 2 rows and 1 columns

x = np.arange(0, 4 * np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)
w = y + z

# make 1st graph
ax[0].plot(x, y, ls='-', label='sin', c='k')
ax[0].plot(x, z, ls='-.', label='cos', c='k')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y, z')
ax[0].set_xlim(0, 4 * np.pi)
ax[0].grid()
ax[0].legend()

# make 2nd graph
ax[1].plot(x, w, color='k', marker=',')
ax[1].set_xlabel('x')
ax[1].set_ylabel('w')
ax[1].set_xlim(0, 4 * np.pi)
ax[1].grid(ls=':')

fig.tight_layout()  # prevent overlapping two graphs
plt.show()
