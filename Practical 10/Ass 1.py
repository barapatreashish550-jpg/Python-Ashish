import pandas as pd

df = pd.read_csv("books.csv")

# a) Print complete report
print("Complete Data:\n", df)

# b) Books of a given author
author_name = input("Enter author name: ")
print("\nBooks by author:\n", df[df['author'] == author_name])

# c) Books by a given publisher
publisher_name = input("Enter publisher name: ")
print("\nBooks by publisher:\n", df[df['publisher'] == publisher_name])

# d) Cheapest and costliest book
print("\nCheapest Book:\n", df.loc[df['price'].idxmin()])
print("\nCostliest Book:\n", df.loc[df['price'].idxmax()])

# e) Sort by year
print("\nSorted by Year:\n", df.sort_values(by='year'))
