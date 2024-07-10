import numpy as np
def longest_string_length(arr):
    return np.max(np.char.str_len(arr))
