import numpy as np
def insert_and_delete(arr, insert_idx, values, delete_idx):
    arr = np.insert(arr, insert_idx, values)
    return np.delete(arr, delete_idx)
