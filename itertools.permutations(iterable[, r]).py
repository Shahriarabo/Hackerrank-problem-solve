from itertools import permutations

def print_permutations(s, r):
    # Compute all possible permutations using itertools.permutations
    perm = permutations(s, r)
    
    # Print the permutations in lexicographic sorted order
    for p in sorted(perm):
        print("".join(p))

# Take input from the user
input_str, size = input().split()
size = int(size)

# Output the permutations of the string in lexicographic sorted order
print_permutations(input_str, size)
