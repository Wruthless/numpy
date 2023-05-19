import matplotlib.pyplot as plt
import numpy as npy

ar_x = npy.array([1, 2, 3, 4, 5])
ar_y = ar_x * 2

plt.title('m = 2')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(ar_x, ar_y)
plt.show()