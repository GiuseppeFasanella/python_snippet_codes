import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

### Generate some data with noise
xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
np.random.seed(1729)
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise
plt.plot(xdata, ydata, 'b-', label='data')
### Now y stores the data we want to fit

### Make the fit
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(xdata, func(xdata, *popt), 'r-',
         label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

popt, pcov = curve_fit(func, xdata, ydata, bounds=(0, [3., 1., 0.5]))
#bounds : 2-tuple of array_like, optional
#Lower and upper bounds on parameters. Defaults to no bounds. 
#Each element of the tuple must be either an array with the length equal to the number of parameters, 
#or a scalar (in which case the bound is taken to be the same for all parameters.) 
#Use np.inf with an appropriate sign to disable bounds on all or some parameters.

plt.plot(xdata, func(xdata, *popt), 'g--',
         label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

###How to force the curve to pass by the first and last point
sigma = np.ones(len(x))
sigma[[0, -1]] = 0.01 ##stai dando un peso 'sostanziale' al primo e all'ultimo punto
#quindi sigma e' una penalty???! (comunque funziona)
popt, pcov = curve_fit(model_func, x, y, p0=(0.1 ,1e-3, 0.1), sigma=sigma)


plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
