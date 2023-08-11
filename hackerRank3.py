if __name__ == "__main__":
    num_records = int(input())
    student_data = {}

    # Input student data
    for _ in range(num_records):
        name, *marks = input().split()
        marks = list(map(float, marks))
        student_data[name] = marks

    query_name = input()

    # Calculate average mark for the queried student
    queried_marks = student_data.get(query_name)
    if queried_marks:
        average_mark = sum(queried_marks) / len(queried_marks)
        print("{:.2f}".format(average_mark))
    else:
        print(queried_marks)

