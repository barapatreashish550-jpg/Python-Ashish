# Create and write names to a file

file = open("names.txt", "w")

file.write("Alice\n")
file.write("Bob\n")
file.write("Charlie\n")

file.close()

print("Names written successfully to names.txt")
