import pandas as pd

df = pd.read_csv("automotive_store.csv")

# a) Print first and last five rows
print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

# b) Clean the dataset
df = df.drop_duplicates()

df = df.dropna()  

df.to_csv("automotive_store_cleaned.csv", index=False)
print("\nDataset cleaned and saved as automotive_store_cleaned.csv")

# c) Find the most expensive automotive part
most_expensive = df.loc[df['Price'].idxmax()]

print("\nMost Expensive Automotive Part:")
print(most_expensive)

# d) Count total automotive parts
total_parts = len(df)

print("\nTotal number of automotive parts:", total_parts)