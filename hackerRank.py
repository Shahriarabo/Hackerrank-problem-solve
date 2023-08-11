def find_runner_up_score(arr):
    # Remove duplicates and sort the list in descending order
    unique_sorted_arr = sorted(set(arr), reverse=True)

    # The second element in the sorted list will be the runner-up score
    runner_up_score = unique_sorted_arr[1]

    return runner_up_score

if __name__ == '__main__':
    # Read input
    n = int(input().strip())  # Number of elements in the array
    arr = list(map(int, input().strip().split()))  # Array of integers

    # Calculate the runner-up score
    runner_up_score = find_runner_up_score(arr)

    # Print the result
    print(runner_up_score)
