def multiply_with_broadcast(arr1, arr2):
    if arr1.shape[1] != arr2.shape[0]:
        raise ValueError("Shapes are incompatible for broadcasting")
    return arr1[:, :arr2.shape[1]] * arr2
