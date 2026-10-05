import numpy as np

# Contiguous memory block with explicit byte strides
arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)

print("Memory Address Pointer:", arr.ctypes.data)
print("Strides (bytes per axis step):", arr.strides)  # Output: (12, 4) -> 12 bytes per row, 4 per item

# Vectorized operation executing in C/SIMD without Python loops
result = arr * 2