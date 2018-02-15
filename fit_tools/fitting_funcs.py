import numpy as np

def exp(x, a, b, c):
    return a * np.exp(-b * x) + c

def pol1(x, a, b):
    return a *x + b
