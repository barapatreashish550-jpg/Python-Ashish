
file = open("data.txt", "r")

content = file.read()


count = len(content)

print("Total number of characters:", count)


file.close()
