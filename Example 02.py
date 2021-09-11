import numpy as np
import time
import sys

s = range(1000)
# S is the list of elements from 0 to 999

print(sys.getsizeof(3) * len(s))
# getSizeOf(3) gives the size occupied by an integer which is multiplied with len of s list to get total size

d = np.arange(1000)
print(d.size*d.itemsize)
# d.size gives size of one element in np array and d.itemsize gives size of the complete np array

# Output:

# 28000
# 4000

# Hence proved that np array consumes less memory
