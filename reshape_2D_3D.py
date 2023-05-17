from numpy import *

data = [[11, 22],
        [23, 24],
        [55, 66]]

data = array(data)
print(data.shape)
print(data, "\n")

# reshape
data = data.reshape((data.shape[0], data.shape[1], 1))
print(data.shape)
print(data)
