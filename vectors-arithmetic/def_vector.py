from numpy import *

v = array([1, 2, 3])
print(v, "\n")

# Add vectors
print("Adding vectors:", "\n")
b = array([1, 2, 3])
print(b, "\n")
c = v + b
print(c, "\n")

# Subtract vectors
print("Subtracting vectors:", "\n")
d = array([0.5, 0.5, 0.5])
print(d, "\n")
e = v - d
print(e, "\n")

# Multiply vectors
print("Multiplying vectors:", "\n")
f = array([2, 2, 2])
print(f, "\n")
g = v * f
print(g, "\n")

# Divide vectors
print("Dividing vectors:", "\n")
h = array([2, 2, 2])
print(h, "\n")
i = v / h
print(i, "\n")