from numpy import *

print("-------------------------------")
print("Summing the matrix array-wise.", "\n")
data = [[1, 2, 3],
        [4, 5, 6]]

data = asarray(data)

print(data, "\n")

# Sum the data array-wise.
result = data.sum(axis=None)
print("Array summation =", result, "\n")

print("-------------------------------")
print("Summing the matrix column-wise.", "\n")

print(data, "\n")

# Sum the data column-wise.
result1 = data.sum(axis=0)
print("Column summation =", result1, "\n")

print("-------------------------------")
print("Summing the matrix row-wise.", "\n")

print(data, "\n")

# Sum the data row-wise.
result2 = data.sum(axis=1)
print("Row summation =", result2, "\n")
