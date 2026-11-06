import student_functions


viewing: bool = True
while viewing:
    user_input = input("What information would you like to see?\n1. Number of student records\n2. Column headings\n3. All student records\n4. Quit\nAnswer: ")
    print("\033[2J\033[H", end="") # Clear the terminal
    if user_input in ["1", "2", "3"]:    
        if user_input == '1':
            print(f"Number of student records: {student_functions.number_of_student_records()}")

        if user_input == '2':
            print(f"Column headings: {student_functions.display_column_headings()}")

        if user_input == '3':
            print(f"Entire file:\n{student_functions.display_all_student_records()}")

    elif user_input == '4':
        viewing = False

    else:
        print("Invalid user input, please try again...")

    print()

print("Bye...")