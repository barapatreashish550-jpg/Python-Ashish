def student_data(student_id, student_name=None, student_class=None):
    print("Student ID:", student_id)

    if student_name:
        print("Student Name:", student_name)

    if student_class:
        print("Student Class:", student_class)


student_data(101)
print()

student_data(102, "Rahul")
print()

student_data(103, "Anita", "10th")