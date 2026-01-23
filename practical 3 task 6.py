n = 5

# Upper half
for i in range(1, n + 1):
    for j in range(i):
        print("* ", end="")
    print("\n")

# Lower half
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("* ", end="")
    print("\n")
    
# Output
# * 

# * * 

# * * * 

# * * * * 

# * * * * * 

# * * * * 

# * * * 

# * * 

# * 
