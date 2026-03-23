import pandas as pd

df = pd.read_csv("sales.csv")

# a) Print list of medical items
print("List of Medical Items:")
print(df[['Item Number', 'Name of Medical Item']])

# b) Print total number of items sold
total_quantity = df['Quantity Sold'].sum()
print("\nTotal Number of Items Sold:", total_quantity)

# c) Print total price of all items sold
df['Total Price'] = df['Price of Medical Item'] * df['Quantity Sold']
total_price = df['Total Price'].sum()

print("\nTotal Price of All Items Sold:", total_price)