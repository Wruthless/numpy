from numpy import inf
from numpy import array
from numpy.linalg import norm

a = array([1, 2, 3])
print(a, "\n")

# calculate norm
maxnorm = norm(a, inf)
print(maxnorm, "\n")
