import numpy as np
from scipy import matrix
from scipy.sparse.linalg import aslinearoperator

M = matrix( [[1,0],[0,1]])
A = aslinearoperator( M )
b = [6, 4]
#bounds on variables if they are not default (x_i > 0)                                                                                                                                  
#Find a way to define bounds on variables                                                                                                                                               
#x0_bounds = (None, None)                                                                                                                                                               
#x1_bounds = (-3, None)                                                                                                                                                                 
from scipy.sparse.linalg import lsqr
x = lsqr(A, b)
print(x[0])
