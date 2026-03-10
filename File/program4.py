
source = open("source.txt", "r")
destination = open("destination.txt", "w")


data = source.read()

destination.write(data)

source.close()
destination.close()


print("File copied successfully.")
