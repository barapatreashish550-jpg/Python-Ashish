import matplotlib.pyplot as plt

candidates = ['A', 'B', 'C', 'D']

votes = [120, 150, 90, 110]

plt.bar(candidates, votes)

plt.xlabel("Candidates")
plt.ylabel("Number of Votes")
plt.title("Public Survey Results")

plt.grid(axis='y')

plt.show()