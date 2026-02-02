# Read 10 integers
arr1 = []
for i in range(10):
    arr1.append(int(input(f"Enter element {i+1}: ")))

# Copy elements in reverse order
arr2 = arr1[::-1]

# Display arrays
print("Original array:", arr1)
print("Reversed array:", arr2)
