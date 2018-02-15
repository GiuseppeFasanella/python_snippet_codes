side_x = [1,2,3] #x points you want to consider                                                                                                                                         
side_y = [4,5,6] #y points you want to consider                                                                                                                                         
X1, X2 = np.meshgrid(side_x, side_y) ##create the 2D grid                                                                                                                               
#X1 = [[1 2 3]                                                                                                                                                                          
#      [1 2 3]                                                                                                                                                                          
#      [1 2 3]]                                                                                                                                                                         

#X2 =[[4 4 4]                                                                                                                                                                           
#     [5 5 5]                                                                                                                                                                           
#     [6 6 6]]                                                                                                                                                                          

size = X1.shape
x1_1d = X1.reshape((1, np.prod(size)))
x2_1d = X2.reshape((1, np.prod(size)))
#x1_1d = [[1 2 3 1 2 3 1 2 3]]                                                                                                                                                          
#x2_1d = [[4 4 4 5 5 5 6 6 6]]                                                                                                                                                          

xdata = np.vstack((x1_1d, x2_1d)) #xdata is the final grid (2D array) xdata = [[x],[y]]                                                                                                 
#xdata = [[1 2 3 1 2 3 1 2 3]                                                                                                                                                           
#         [4 4 4 5 5 5 6 6 6]]                                                                                                                                                          

from fitting_funcs import plane
z = plane(xdata, *(0.4,0.3,0.7))
#z = [ 2.3  2.7  3.1  2.6  3.   3.4  2.9  3.3  3.7]                                                                                                                                     

Z = z.reshape(size)
#Z = [[ 2.3  2.7  3.1]                                                                                                                                                                  
#     [ 2.6  3.   3.4]                                                                                                                                                                  
#     [ 2.9  3.3  3.7]]   
