# Open the file in read mode
file = open("words.txt", "r")

count = 0

# Read each line from the file
for line in file:
    words = line.lower().split()   # Convert to lowercase and split into words
    count = count + words.count("the")

# Close the file
file.close()

# Print the result
print("The word 'the' appears", count, "times.")