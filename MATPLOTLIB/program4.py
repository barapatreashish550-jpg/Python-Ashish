import matplotlib.pyplot as plt

heights = []
weights = []

with open("data.txt", "r") as file:
    for line in file:
        h, w = map(float, line.split())  
        heights.append(h)
        weights.append(w)

plt.scatter(heights, weights)

plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Height vs Weight Scatter Plot")

plt.grid()

plt.show()