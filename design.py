def door_mat_pattern(rows, columns):
    # Design the top part of the door mat
    for i in range(1, rows, 2):
        print((".|." * i).center(columns, "-"))

    # Print the welcome message
    print("WELCOME".center(columns, "-"))

    # Design the bottom part of the door mat
    for i in range(rows - 2, -1, -2):
        print((".|." * i).center(columns, "-"))

# Test with the given sample input
if __name__ == "__main__":
    rows, columns = map(int, input().split())
    door_mat_pattern(rows, columns)
