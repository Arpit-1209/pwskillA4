import numpy as np

# Given NumPy array
array = np.array([10, 15, 20, 25, 30])

# Filtering elements which are divisible by 3
filtered_array = array[array % 3 == 0]
print("Filtered Array:", filtered_array)
