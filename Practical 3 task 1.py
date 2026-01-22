for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")

# Output  
# 1 

# 1 2 

# 1 2 3 

# 1 2 3 4 

# 1 2 3 4 5 


for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print("\n")
    
# Output
# 1 

# 2 2 

# 3 3 3 

# 4 4 4 4 

# 5 5 5 5 5 


for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("\n")

#Output
# 1 

# 2 1 

# 3 2 1 

# 4 3 2 1 

# 5 4 3 2 1 


for i in range(1, 6):
    for j in range(i):
        if j % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print("\n")
    
# Output
# 1 

# 1 0 

# 1 0 1 

# 1 0 1 0 

# 1 0 1 0 1 


num = 2
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 2
    print("\n")
    
# Output
# 2 

# 4 6 

# 8 10 12 

# 14 16 18 20 



for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print("\n")
    
# Output
# * 

# * * 

# * * * 

# * * * * 

# * * * * * 