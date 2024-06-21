from os import chdir
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from matplotlib.animation import FuncAnimation, PillowWriter
from numpy import arange, meshgrid, sqrt, sin
from matplotlib.ticker import FormatStrFormatter

# Data set
X = arange(start = -5, stop = 5, step = 0.25)
Y = arange(start = -5, stop = 5, step = 0.25)
X, Y = meshgrid(X, Y)
R = sqrt(X**2 + Y**2)
Z = sin(R)

# Surface
fig, ax = plt.subplots(subplot_kw = {"projection": "3d"})
surf = ax.plot_surface(X, Y, Z, cmap = cm.coolwarm, linewidth = 0, antialiased = False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.set_title(label = r'$\sin \left( \sqrt{x^2 + y^2} \right)$', fontsize = 16)
fig.colorbar(surf, shrink = 0.5, aspect = 5)

def animate(i):
    ax.view_init(azim = i)


chdir('F:') # set working directory
ani = FuncAnimation(fig, animate, frames = 100)    
ani.save("Surface_Python.gif", dpi = 200, writer = PillowWriter(fps = 25))



