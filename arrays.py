import numpy as npy

ar = npy.array([[12, 34, 56], [34, 33, 67]], dtype=float)

Ar = npy.array([[12, 34, 56], [34, 33, 67]], dtype=float)
ad5 = Ar + 5

ar_1 = npy.array([1, 23, 45, 6])
ar_2 = npy.array([[1, 2, 3],
                  [2, 5, 6]])

# 2 two-dimensional arrays.
ar_3 = npy.array([[[1, 2, 3],
                   [2, 5, 6]],
                  [[1, 2, 3],
                   [2, 5, 6]]])

# print(ar)
# print(ad5)

# 1-D array
# Access second element of ar (34)
print(ar_1[1])

# 2-D array
# Access last element of second array (6) in the two-dimensional array.
print(ar_2[1, 2])

# 2 2-D arrays
# Access the second element of the first array in the first two-dimensional array.
print(ar_3[0, 0, 1])
