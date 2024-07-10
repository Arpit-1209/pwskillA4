import numpy as np
arr = np.array([1, 2, 3])
swapped_arr = arr.newbyteorder('<' if arr.dtype.byteorder == '>' else '>')
