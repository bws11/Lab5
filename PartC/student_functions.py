import csv

def read_csv_file() -> str:
    with open('PartC/student-Ai-CSV.csv', 'r', encoding='utf-8', newline='') as f:
        file = csv.reader(f)

        file_contents = ''
        for row in file:
            file_contents += ', '.join(row)
            file_contents += '\n'
    return file_contents

def number_of_student_records():
    # -1 because of the headers
    return int(read_csv_file().count('\n')) - 1

def display_column_headings():
    # Split into new lines, then take the first one which is the header
    return read_csv_file().split('\n')[0]

def display_all_student_records():
    return read_csv_file()

if __name__ == '__main__':
    print(display_column_headings())