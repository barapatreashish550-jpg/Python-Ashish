class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

s1 = Student("Rahul", 75)

print("Original Values")
print("Student Name:", s1.student_name)
print("Marks:", s1.marks)

s1.student_name = "Amit"
s1.marks = 85

print("\nModified Values")
print("Student Name:", s1.student_name)
print("Marks:", s1.marks)