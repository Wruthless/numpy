from numpy import *

l = [1.0, 2.0, 3.0, 4.0, 5.0]
a = array(l)

# Display array.
print(a)

# Display shape.
print(a.shape)

# Display data type.
print(a.dtype)

# Using empty() to generate an array.
arr = empty([3, 3])
print(arr)

# Using zeros() to generate an array.
arr_z = zeros([3, 5])
print(arr_z)

# Using ones() to generate an array.
arr_ones = ones([5])
print(arr_ones)