# Open grades.txt in read mode
file = open("grades.txt", "r")

# Open passed.txt in write mode
passed = open("passed.txt", "w")

# Read each line from the file
for line in file:
    data = line.split()      # Split name and grade
    name = data[0]
    grade = data[1]

    if grade == "A" or grade == "B":
        passed.write(name + "\n")

# Close both files
file.close()
passed.close()

print("Passed students written to passed.txt")