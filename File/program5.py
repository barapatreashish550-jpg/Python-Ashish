# Open the file in append mode
file = open("names.txt", "a")

# Write the new name
file.write("\nDavid")

# Close the file
file.close()

print("Name added successfully.")