import numpy as np

# Define the shapes of the matrices
shape_C = (3, 2)
shape_D = (2, 4)

# Create two matrices C and D with random integers
C = np.random.randint(1, 10, size=shape_C)
D = np.random.randint(1, 10, size=shape_D)

# Perform matrix multiplication
result = np.dot(C, D)

print("Matrix C:\n", C)
print("Matrix D:\n", D)
print("Matrix C * D:\n", result)
