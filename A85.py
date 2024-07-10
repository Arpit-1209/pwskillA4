import numpy as np

# Define the shape of the square matrix G
n = 3  # Example size of the square matrix

# Create the square matrix G with random integers
G = np.random.randint(1, 10, size=(n, n))

# Compute the inverse of the matrix G
# First, we need to ensure the matrix is invertible by checking if its determinant is not zero
if np.linalg.det(G) == 0:
    print("Matrix G is not invertible.")
else:
    G_inverse = np.linalg.inv(G)
    print("Matrix G:\n", G)
    print("Inverse of Matrix G:\n", G_inverse)
