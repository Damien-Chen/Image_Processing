import numpy as np

x = np.array([1, 2, 4, 3, 2, 1, 1])
h = np.array([1, 2, 3, 1, 1])

y = np.convolve(x,h,'full')

print("Convolution y = ", y)
