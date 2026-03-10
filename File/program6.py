# Open the file in read mode
file = open("numbers.txt", "r")

total = 0

# Read each line in the file
for line in file:
    num = int(line.strip())   # Convert line to integer
    total = total + num       # Add to total

# Close the file
file.close()

# Print the sum
print("Sum of numbers:", total)