import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,4*np.pi,0.1)
y=np.sin(x)

fig, ax = plt.subplots() # generate an object of figure and axes
ax.plot(x,y) # generate a graph in the axes object
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid()
plt.show()


# plt.plot(x,y) #plot by x in horizontal, y in vertical
# plt.xlabel('x') # set a label for x axis
# plt.ylabel('y') # set it for y axis
# plt.grid() # draw grid
# plt.show()
