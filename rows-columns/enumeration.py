from numpy import *

data = [[1, 2, 3], [4, 5, 6]]

print("----------------------------------------------\n")
print("Enumerate the rows of the matrix.")

# Convert to numpy array.
data = asarray(data)

print(data.shape[0], "\n")

for row in range(2):
    print(data[row, :])

print()

print(data[0, :], "\n")

for row in range(data.shape[0]):
    print(data[row, :])

print("----------------------------------------------\n")
print("Enumerate the columns of the matrix.")

for column in range(data.shape[1]):
    print(data[:, column])
