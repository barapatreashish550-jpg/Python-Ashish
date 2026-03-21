import pandas as pd

# Create DataFrame
data = {
    'State': ['Maharashtra', 'Gujarat', 'Karnataka', 'Rajasthan', 'Punjab'],
    'Area': [307713, 196024, 191791, 342239, 50362],   # in sq km
    'Population': [112374333, 60439692, 61095297, 68548437, 27743338]
}

df = pd.DataFrame(data)

# a) Complete information
print("Complete Data:\n", df)

# b) State with largest area
print("\nState with Largest Area:\n", df.loc[df['Area'].idxmax()]['State'])

# c) State with largest population
print("\nState with Largest Population:\n", df.loc[df['Population'].idxmax()]['State'])

# d) Calculate population density
df['Density'] = df['Population'] / df['Area']
print("\nWith Density:\n", df)

# e) State with highest density
print("\nState with Highest Density:\n", df.loc[df['Density'].idxmax()]['State'])