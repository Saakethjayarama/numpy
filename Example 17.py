# Stack a np array on another

import numpy as np

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[7,8,9],[10,11,12]])

print(np.vstack((a, b))) # Verticle stacking
print(np.hstack((a, b))) # Horizontal stacking
print(a.ravel()) # Make np array to 1d array
