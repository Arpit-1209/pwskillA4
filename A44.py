import numpy as np
def moving_sum(arr, window_size):
    return np.array([np.sum(arr[i:i+window_size]) for i in range(len(arr) - window_size + 1)])
