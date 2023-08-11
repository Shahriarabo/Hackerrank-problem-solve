from itertools import combinations

def print_sorted_combinations(string, r):
    # Generate all combinations up to size r
    for i in range(1, r + 1):
        # Use combinations function to generate combinations of size i
        for combination in combinations(sorted(string), i):
            # Join the elements of the combination and print them
            print(''.join(combination))

if __name__ == "__main__":
    input_string, r = input().split()
    r = int(r)
    print_sorted_combinations(input_string, r)
