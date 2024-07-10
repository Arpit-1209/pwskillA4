import numpy as np

# Define the shape of the matrix E
shape_E = (3, 4)

# Create the matrix E with random integers
E = np.random.randint(1, 10, size=shape_E)

# Find the transpose of the matrix E
E_transpose = E.T

print("Matrix E:\n", E)
print("Transpose of Matrix E:\n", E_transpose)
