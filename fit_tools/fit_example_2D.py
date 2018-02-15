# curvefit with non linear least squares (curve_fit function)                                                                                                                           
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from fitting_funcs import plane

limits = [1,3,4,6]
side_x = np.linspace(limits[0], limits[1], 5)
side_y = np.linspace(limits[2], limits[3], 5)
X1, X2 = np.meshgrid(side_x, side_y)
size = X1.shape
x1_1d = X1.reshape((1, np.prod(size))) #x1_1d = [[x]]                                                                                                                                   
x2_1d = X2.reshape((1, np.prod(size))) #x2_1d = [[y]]                                                                                                                                   

xdata = np.vstack((x1_1d, x2_1d)) #xdata is the final grid (2D array) xdata = [[x],[y]]                                                                                                 

original = (1,2,3) #injected coefficients                                                                                                                                               
z = plane(xdata, *original)
Z = z.reshape(size)
z_noise = z + .2*np.random.randn(len(z))
Z_noise = z_noise.reshape(size)

zdata = z_noise
popt, pcov = curve_fit(plane, xdata, zdata)
#xdata=[[ 1. 1.5 2 ....]
#       [ y y y y y y  ]
#zdata=[ z1 z2 ........]
print "original: {}\nfitted: {}".format(original, popt)
z_fit = plane(xdata, *popt)
Z_fit = z_fit.reshape(size)

###Plot                                                                                                                                                                                 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig = plt.figure()
ax = fig.gca(projection='3d')
surf_or = ax.plot_surface(X1, X2, Z, cmap=cm.Greys,
                       linewidth=0, antialiased=False)
surf = ax.plot_surface(X1, X2, Z_fit, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
fig.colorbar(surf_or, shrink=0.5, aspect=5)
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
