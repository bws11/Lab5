import student_functions

print("What information would you like to see?")
number_of_student_records = input("Would you like to see the number of student records (y/n)? ")
column_headings = input("Would you like to see the column headings (y/n)? ")
student_records = input("Would you like to see all the student records (y/n)? ")


if number_of_student_records.lower() == 'y':
    print(f"Number of student records: {student_functions.number_of_student_records()}")

if column_headings.lower() == 'y':
    print(f"Column headings: {student_functions.display_column_headings()}")

if student_records.lower() == 'y':
    print(f"Entire file:\n{student_functions.display_all_student_records()}")