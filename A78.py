import numpy as np
array_a = np.arange(1, 13).reshape((4, 3))
view_b = array_a[:2, :2]
view_b += 5
# Check if array_a is affected
is_array_a_affected = np.array_equal(array_a[:2, :2], view_b)
