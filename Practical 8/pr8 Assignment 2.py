
source = input("Enter source python file name: ")
destination = input("Enter destination file name: ")

with open(source, "r") as f1, open(destination, "w") as f2:
    for line in f1:
    
        if not line.strip().startswith("#"):
            f2.write(line)

print("\n--- Source File Content ---")
with open(source, "r") as f:
    print(f.read())

print("\n--- Destination File Content (Without Comments) ---")
with open(destination, "r") as f:
    print(f.read())