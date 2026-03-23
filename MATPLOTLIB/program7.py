import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("EV_Population.csv")

make_counts = df['Make'].value_counts().head(10)  # Top 10 makes

plt.figure()
plt.bar(make_counts.index, make_counts.values)
plt.xlabel("EV Make")
plt.ylabel("Count")
plt.title("Top 10 EV Manufacturers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


type_counts = df['Electric Vehicle Type'].value_counts()

plt.figure()
plt.pie(type_counts.values, labels=type_counts.index, autopct='%1.1f%%')
plt.title("Distribution of EV Types")
plt.show()

plt.figure()
plt.hist(df['Electric Range'].dropna(), bins=20)
plt.xlabel("Electric Range (miles)")
plt.ylabel("Number of Vehicles")
plt.title("Distribution of Electric Range")
plt.grid()
plt.show()