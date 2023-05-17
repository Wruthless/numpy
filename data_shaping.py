import numpy
from numpy import *

data = array([11, 22, 33, 44, 55])
print(data.shape)

dataset = [
    [11, 22],
    [33, 44],
    [55, 66]
]
d = array(dataset)
print(d.shape)

print('Rows: %d' % d.shape[0])
print('Columns: %d' % d.shape[1])
print()
print()

print(data.shape)
data = data.reshape((data.shape[0], 1))
print(data.shape)


