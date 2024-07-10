import numpy as np
data = np.random.randint(1, 10, size=(3, 4))
data_copy = data[data > 5].copy()
data_copy[0] = 99
# Check if data is affected
is_data_affected = 99 in data
