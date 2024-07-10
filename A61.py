import numpy as np
def dataset_statistics():
    arr = np.random.randint(1, 1001, 100)
    mean = np.mean(arr)
    median = np.median(arr)
    variance = np.var(arr)
    std_dev = np.std(arr)
    return mean, median, variance, std_dev
