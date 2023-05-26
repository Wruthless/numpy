import numpy as np
from scipy.integrate import quad
from scipy.stats import norm

mean = 155.7
std_dev = 6.6

lower_limit = 142.5
upper_limit = 155.7


def gaussian(x):
    return norm.pdf(x, mean, std_dev)


result = quad(gaussian, lower_limit, upper_limit)

area = result[0]

print(area)
