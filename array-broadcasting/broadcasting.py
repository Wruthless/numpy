from numpy import *

print("----------------------------------------------------------------")
print("Adding scalar to one dimensional array.""\n")
a = array([1, 2, 3])
print(a, "\n")

# scalar
b = 2
print(b, "\n")

# broadcast
c = a + b
print(c, "\n")

print("----------------------------------------------------------------")
print("Adding scalar to two dimensional array.""\n")
d = array([[1, 2, 3],
           [4, 5, 6]])

# scalar
e = 2

f = e + d
print(f, "\n")

print("----------------------------------------------------------------")
print("Adding one dimensional array to two dimensional array.""\n")
g = array([[1, 2, 3],
           [4, 5, 6]])

h = array([1, 2, 3])

i = g + h
print(i, "\n")
