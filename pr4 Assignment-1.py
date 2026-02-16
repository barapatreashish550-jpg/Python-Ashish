#a)Construct a python program using NumPy to generate a 4x4 identity matrix.
import numpy as np

# Generate a 4x4 identity matrix
identity_matrix = np.identity(4)

print("4x4 Identity Matrix:")
print(identity_matrix)





#b)Construct a python program to generate two 3x3 matrices filled with random integers(1 to 9), then perform matrix addition and matrix multiplication.
import numpy as np

# Generate two 3x3 matrices with random integers from 1 to 9
matrix1 = np.random.randint(1, 10, (3, 3))
matrix2 = np.random.randint(1, 10, (3, 3))

# Matrix addition
addition = matrix1 + matrix2

# Matrix multiplication
multiplication = np.dot(matrix1, matrix2)

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nMatrix Addition:")
print(addition)

print("\nMatrix Multiplication:")
print(multiplication)
