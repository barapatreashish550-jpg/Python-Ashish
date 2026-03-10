# Open the file in read mode
file = open("data.txt", "r")

# Read the entire content of the file
content = file.read()

# Count the number of characters
count = len(content)

# Print the count
print("Total number of characters:", count)

# Close the file
file.close()