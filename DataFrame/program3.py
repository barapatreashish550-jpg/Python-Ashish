import pandas as pd


df = pd.read_excel("employee.xlsx")

# a) Employees working in "Automotive" domain
print("Employees in Automotive Domain:")
auto_emp = df[df['Department'] == "Automotive"]
print(auto_emp)

# b) Details of employee by Employee ID 
emp_id = int(input("\nEnter Employee ID: "))
emp_details = df[df['Employee ID'] == emp_id]

if not emp_details.empty:
    print("\nEmployee Details:")
    print(emp_details)
else:
    print("Employee not found!")

# d) List of all Developers
print("\nList of Developers:")
developers = df[df['Designation'] == "Developer"]
print(developers)