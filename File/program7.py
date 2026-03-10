
file = open("words.txt", "r")

count = 0
for line in file:
    words = line.lower().split()  
    count = count + words.count("the")

file.close()
print("The word 'the' appears", count, "times.")
