# Open source file in read mode
source = open("source.txt", "r")

# Open destination file in write mode
destination = open("destination.txt", "w")

# Read content from source file
data = source.read()

# Write content to destination file
destination.write(data)

# Close both files
source.close()
destination.close()

print("File copied successfully.")