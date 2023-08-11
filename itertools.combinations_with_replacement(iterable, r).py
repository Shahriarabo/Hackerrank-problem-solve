from itertools import combinations_with_replacement

def print_sorted_combinations_with_replacement(string, r):
    # Use combinations_with_replacement function to generate combinations with replacements of size r
    for combination in combinations_with_replacement(sorted(string), r):
        # Join the elements of the combination and print them
        print(''.join(combination))

if __name__ == "__main__":
    input_string, r = input().split()
    r = int(r)
    print_sorted_combinations_with_replacement(input_string, r)
