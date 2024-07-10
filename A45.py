import numpy as np
def all_even_columns(arr):
    return np.all(arr % 2 == 0, axis=0)
