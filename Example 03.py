import numpy as np
import time
import sys


SIZE = 100000
list1 = range(SIZE)
list2 = range(SIZE)

npList1 = np.arange(SIZE)
npList2 = np.arange(SIZE)

start = time.time()
result = [(x, y) for x, y in zip(list1, list2)] # list comprehension
print('Time taken to add by list is ', (time.time()-start)*1000)

start = time.time()
result = npList1 + npList2
end = time.time()
print('Time taken to add by np array is ', (time.time()-start)*1000)



# (env) L:\AI & ML\Numpy>python "Example 03.py"
# Time taken to add by list is  22.04442024230957
# Time taken to add by np array is  5.976676940917969

# Hence proved that,
# - To add list in list it takes whole lot of process but in np array it's just + operator hence convenient
# - Time taken to add 2 np arrays are way less than time taken to add by lists
