from numpy import *

data = array([
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]
])

# separate data
X, y = data[:, :-1], data[:, -1]
print(X)
print()
print(y)

print()
print()
dataset = array([
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]
])

split = 2
train, test = dataset[:split, :], dataset[split:, :]
print(train)
print(test)
