# Open the file in read mode
file = open("names.txt", "r")

# Read each line and print it
for line in file:
    print(line.strip())

# Close the file
file.close()