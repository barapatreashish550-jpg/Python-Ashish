
file = open("grades.txt", "r")
passed = open("passed.txt", "w")

for line in file:
    data = line.split()      
    name = data[0]
    grade = data[1]

    if grade == "A" or grade == "B":
        passed.write(name + "\n")

file.close()
passed.close()


print("Passed students written to passed.txt")
