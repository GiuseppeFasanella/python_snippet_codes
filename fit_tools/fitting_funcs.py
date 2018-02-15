import numpy as np

def exp(x, a, b, c):
    return a * np.exp(-b * x) + c

def pol1(x, a, b):
    return a *x + b

def plane(x, a, b, c):
    #x is the 2-d grid                                                                                                                                                                  
    #x[0] is the "x"-coordinate                                                                                                                                                           
    #x[1] is the "y"-coordinate                                                                                                                                                           
    return a*x[0] + b*x[1] + c
