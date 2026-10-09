import numpy as np
from scipy import linalg, optimize

# Define a linear system Ax = b
A = np.array([[3, 2], [1, 2]], dtype=np.float64)
b = np.array([[5], [5]], dtype=np.float64)

# Directly calls low-level LAPACK routine 'dgesv' in C/Fortran
x = linalg.solve(A, b)
print("Solved System (x):", x.ravel())

# Fast optimization kernel
res = optimize.minimize(lambda v: (v[0]-1)**2 + (v[1]-2.5)**2, [0, 0])
print("Optimization Minimum:", res.x)