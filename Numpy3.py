
n = int(input("Enter number of elements: "))


arr = []
for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    arr.append(value)


max_diff = abs(arr[0] - arr[1])
min_diff = abs(arr[0] - arr[1])

max_pair = (arr[0], arr[1])
min_pair = (arr[0], arr[1])

for i in range(n):
    for j in range(i + 1, n):
        diff = abs(arr[i] - arr[j])

        if diff > max_diff:
            max_diff = diff
            max_pair = (arr[i], arr[j])

        if diff < min_diff:
            min_diff = diff
            min_pair = (arr[i], arr[j])


print("\nArray Elements:", arr)
print("Pair with Maximum Difference:", max_pair, "Difference:", max_diff)
print("Pair with Minimum Difference:", min_pair, "Difference:", min_diff)
