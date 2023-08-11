if __name__ == "__main__":
    num_students = int(input(""))
    student_data = {}

    for _ in range(num_students):
        name = input("Enter student name: ")
        grade = float(input("Enter student grade: "))
        student_data[name] = grade

    # Find the second-lowest grade
    grades =list(student_data.values())
    second_lowest_grade = sorted(set(grades))[1]

    # Find students with the second-lowest grade
    second_lowest_students =[name for name, grade in student_data.items() if grade == second_lowest_grade]

    # Sort the names alphabetically and print them
    second_lowest_students.sort()
    for name in second_lowest_students:
        print(name)
