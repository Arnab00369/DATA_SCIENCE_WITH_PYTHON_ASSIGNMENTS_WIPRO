# Question: Exercise 1: Create two dimensional 3*3 array and perform ndim, shape, slicing operation on it.

import numpy as np

# create 2D 3x3 array
arr_2d = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

# number of dimensions
print("Dimensions (ndim):", arr_2d.ndim)

# shape of the array
print("Shape:", arr_2d.shape)

# slicing examples
print("First row:", arr_2d[0])          # full first row
print("First column:", arr_2d[:,0])     # full first column
print("Sub-matrix (2x2):\n", arr_2d[0:2, 0:2])  # top-left 2x2 block
