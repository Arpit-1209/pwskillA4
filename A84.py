import numpy as np

# Define the shape of the square matrix F
n = 3  # Example size of the square matrix

# Create the square matrix F with random integers
F = np.random.randint(1, 10, size=(n, n))

# Compute the determinant of the matrix F
det_F = np.linalg.det(F)

print("Matrix F:\n", F)
print("Determinant of Matrix F:", det_F)
