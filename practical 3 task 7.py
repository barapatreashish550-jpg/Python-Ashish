while True:
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    if start >= 1 and end >= start:
        break
    else:
        print("Invalid input! Start should be >= 1 and end should be >= start.")

print("Prime numbers between", start, "and", end, "are:")

# Check prime numbers using for loop
for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
            
# Output
# Enter the starting number: 10
# Enter the ending number: 30
# Prime numbers between 10 and 30 are:
# 11 13 17 19 23 29 
