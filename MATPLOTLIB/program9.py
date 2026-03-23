import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("sales.csv")

plt.plot(df['Month'], df['Sales'], marker='o')

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")

plt.grid()

plt.show()

peak = df.loc[df['Sales'].idxmax()]
print("Peak Sales Month:", peak['Month'], "with Sales:", peak['Sales'])