import numpy as np
arr1 = np.array([1,2,3,4,4,5])
arr2 = np.array([5,6,7,7,8,9])
arr = np.concatenate((arr1, arr2))
print(arr)
