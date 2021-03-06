https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html
  
>>> from scipy.optimize import least_squares

>>> def fun(x, t, y): #x are the parameters, t and y are the inputs
        ## Note that the function must return the vector of the residuals!!!
...     return x[0] + x[1] * np.exp(x[2] * t) - y
...
>>> x0 = np.array([1.0, 1.0, 0.0]) #x0 are the initial parameters
Compute a standard least-squares solution:

>>>
>>> res_lsq = least_squares(fun, x0, args=(t_train, y_train))

>>> res_1.x
array([ 1.,  1.])
>>> res_1.cost
9.8669242910846867e-30
>>> res_1.optimality
