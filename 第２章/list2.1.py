import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 4 * np.pi, 0.1)
y = np.sin(x)
plt.plot(x, y)  # plot by x in horizontal, y in vertical
plt.xlabel('x')  # set a label for x axis
plt.ylabel('y')  # set it for y axis
plt.grid()  # draw grid
plt.show()
