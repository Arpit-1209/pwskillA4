import numpy as np

# Creating a NumPy array of integers
array = np.array([10, 20, 30, 40, 50])

# Finding the index of a specific element (e.g., 30)
index = np.where(array == 30)
print("Index of 30:", index[0][0])
