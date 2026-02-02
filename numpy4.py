import numpy as np

# Define arrays
array1 = np.array([0, 10, 20, 40, 60, 80])
array2 = np.array([10, 30, 40, 50, 70, 90])

# Find set difference
result = np.setdiff1d(array1, array2)

# Display output
print("Array1:", array1)
print("Array2:", array2)
print("Set difference between two arrays:")
print(result)
