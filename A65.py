import numpy as np

# Creating an array of 50 integers between 10 and 1000
array = np.random.randint(10, 1001, 50)

# Calculating percentiles
percentile_10th = np.percentile(array, 10)
median = np.median(array)
percentile_90th = np.percentile(array, 90)
first_quartile = np.percentile(array, 25)
third_quartile = np.percentile(array, 75)

print("10th Percentile:", percentile_10th)
print("50th Percentile (Median):", median)
print("90th Percentile:", percentile_90th)
print("1st Quartile:", first_quartile)
print("3rd Quartile:", third_quartile)
