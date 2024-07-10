import numpy as np
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
copy_arr = arr1.copy()
copy_arr[0] = 99
# Check if arr1 is affected
is_arr1_affected = (arr1[0] == 99)
