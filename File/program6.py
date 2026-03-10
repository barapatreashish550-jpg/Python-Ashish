
file = open("numbers.txt", "r")

total = 0

for line in file:
    num = int(line.strip())   
    total = total + num       

file.close()
print("Sum of numbers:", total)
