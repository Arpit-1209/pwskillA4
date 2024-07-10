import numpy as np
orig_array = np.arange(1, 9).reshape((2, 4))
reshaped_view = orig_array.reshape((4, 2))
reshaped_view[0, 0] = 99
# Check if orig_array is affected
is_orig_array_affected = (orig_array[0, 0] == 99)
