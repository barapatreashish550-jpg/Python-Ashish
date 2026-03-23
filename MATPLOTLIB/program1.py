import matplotlib.pyplot as plt

# Generate x values from -10 to 10
x = list(range(-10, 11))

# Calculate corresponding y values
y = [2*i + 3 for i in x]

# Plot the graph
plt.plot(x, y)

# Add labels and title
plt.xlabel("x values")
plt.ylabel("y = 2x + 3")
plt.title("Graph of y = 2x + 3")

# Show grid
plt.grid()

# Display the plot
plt.show()