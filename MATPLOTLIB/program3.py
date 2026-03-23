import matplotlib.pyplot as plt

scores = [45, 67, 78, 89, 90, 56, 72, 68, 99, 82, 61, 74, 88, 53, 47, 69, 77, 84, 92, 58]

bins = range(0, 101, 10)

plt.hist(scores, bins=bins)

plt.xlabel("Score Range")
plt.ylabel("Number of Students")
plt.title("Distribution of Student Scores")

plt.grid()
plt.show()