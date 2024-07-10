import numpy as np
matrix = np.random.randint(1, 10, size=(3, 3))
view_slice = matrix[:2, :2]
view_slice[0, 0] = 99
# Check if matrix is affected
is_matrix_affected = (matrix[0, 0] == 99)
