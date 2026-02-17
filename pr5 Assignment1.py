
nums = input("Enter a series of integers separated by space: ")
t = tuple(map(int, nums.split()))

# a) Print total number of items in the tuple
print("Total number of items in the tuple:", len(t))

# b) Print the last item in the tuple
if len(t) > 0:
    print("Last item in the tuple:", t[-1])
else:
    print("Tuple is empty")

# c) Print the tuple elements in reverse order
print("Tuple elements in reverse order:", t[::-1])

# d) Check if integer 5 is present in the tuple
if 5 in t:
    print("Yes")
else:
    print("No")

# e) Remove first and last items, sort remaining items, and print result
if len(t) > 2:
    remaining = list(t[1:-1])
    remaining.sort()
    print("Sorted tuple after removing first and last items:", tuple(remaining))
else:
    print("Not enough elements to remove first and last items")
