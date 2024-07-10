import numpy as np
arr = np.array([1, 2, 3])
is_swapping_necessary = arr.dtype.byteorder not in ('=', '|')
