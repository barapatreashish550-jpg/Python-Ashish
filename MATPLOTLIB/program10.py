import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("pollution.csv")


plt.figure()
plt.plot(df['Month'], df['PM2.5'], marker='o', label='PM2.5')
plt.plot(df['Month'], df['PM10'], marker='o', label='PM10')

plt.xlabel("Month")
plt.ylabel("Pollution Level")
plt.title("Air Pollution Trends Over Months")
plt.legend()
plt.grid()
plt.show()

x = range(len(df['Month']))

plt.figure()
plt.bar(x, df['PM2.5'], label='PM2.5')
plt.bar(x, df['PM10'], bottom=df['PM2.5'], label='PM10')  # stacked bar

plt.xticks(x, df['Month'])
plt.xlabel("Month")
plt.ylabel("Pollution Level")
plt.title("PM2.5 vs PM10 Comparison")
plt.legend()
plt.show()