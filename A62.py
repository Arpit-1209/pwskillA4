import numpy as np
arr = np.random.randint(1, 101, size=50)
percentile_25 = np.percentile(arr, 25)
percentile_75 = np.percentile(arr, 75)
