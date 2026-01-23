n = 5

for i in range(1, n + 1):
    # print leading spaces
    print(" " * (n - i), end="")
    
    # print stars with two spaces
    for j in range(i):
        print("*  ", end="")
    
    print("\n")
    
# Output
#   *  

#   *  *  

#   *  *  *  

#  *  *  *  *  

# *  *  *  *  *  
