import numpy as np

# Define the shape of the matrices
shape = (3, 3)

# Create two matrices A and B with random integers
A = np.random.randint(1, 10, size=shape)
B = np.random.randint(1, 10, size=shape)

# Perform addition
C_add = A + B

# Perform subtraction
C_sub = A - B

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix A + B:\n", C_add)
print("Matrix A - B:\n", C_sub)
