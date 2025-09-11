# Question:Exercise 2 : Create one dimensional array and perform ndim, shape, reshape operation on it.

import numpy as np

# create 1D array
arr_1d = np.array([10, 20, 30, 40, 50, 60])

# number of dimensions
print("Dimensions (ndim):", arr_1d.ndim)

# shape of the array
print("Shape:", arr_1d.shape)

# reshape the 1D array into 2 rows, 3 columns
reshaped_arr = arr_1d.reshape(2, 3)
print("Reshaped Array (2x3):\n", reshaped_arr)
