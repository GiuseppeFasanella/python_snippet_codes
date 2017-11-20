######This is to find a solution for Ax=b, in the sense of the least squares
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

######Solve linear equation set #######
#La condizione e' che la matrice sia non-degenere e quadrata
import numpy as np
a = np.array([[3,1], [1,2]])
b = np.array([9,8])
x = np.linalg.solve(a, b)
print(x)

print(np.allclose(np.dot(a, x), b))

######Linear optimization problem #########
#Problem is to minimize c*x
#bound on the x vector
#plus additional constraints: Ax<b
c = [-1, 4]
A = [[-3, 1], [1, 2]]
b = [6, 4]
#bounds on variables if they are not default (x_i > 0)                                                                                                                                  
x0_bounds = (None, None)
x1_bounds = (-3, None)
from scipy.optimize import linprog
res = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds),
              options={"disp": True}) #disp is verbosity                                                                                                                                
print(res)
