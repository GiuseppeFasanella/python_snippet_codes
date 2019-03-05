a = np.array([-1, 0, 1, 2, 3], dtype=float)
b = np.array([ 0, 0, 0, 2, 2], dtype=float)

# If you don't pass `out` the indices where (b == 0) will be uninitialized!
c = np.divide(a, b, out=np.zeros_like(a), where=b!=0)
[ 0.   0.   0.   1.   1.5]
