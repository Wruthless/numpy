import math

# given values
λ = 12
k = 15

# probability calculation
P = ((λ ** k) * math.exp(-λ)) / math.factorial(k)

print(P)
