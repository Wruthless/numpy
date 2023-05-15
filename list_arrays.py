from numpy import *

data = [11, 22, 33, 44, 55]
data = array(data)
print(data)
print(type(data))

data_a = [[11, 22], [33, 44], [55, 66]]
dat_a = array(data_a)
print(dat_a)
print(type(dat_a))

# Indexing
print(data[0])
print(data[4])

# Negative Indexing
print(data[-1])
print(data[-5])