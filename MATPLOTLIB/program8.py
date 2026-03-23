import pandas as pd

df = pd.read_excel("employee.xlsx")

print("\nEmployees in Automotive Domain:\n")
auto_emp = df[df['Department'] == "Automotive"]
print(auto_emp)

emp_id = int(input("\nEnter Employee ID to search: "))
emp_details = df[df['Employee ID'] == emp_id]

print("\nEmployee Details:\n")
if not emp_details.empty:
    print(emp_details)
else:
    print("Employee not found!")

print("\nList of Developers:\n")
developers = df[df['Designation'] == "Developer"]
print(developers)