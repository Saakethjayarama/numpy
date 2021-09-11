# Axis
# Rows = Axis 1
# Columns = Axis 0

import numpy as np

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(a.sum(axis=0))
print(a.min(axis=0))
print(a.max(axis=0))