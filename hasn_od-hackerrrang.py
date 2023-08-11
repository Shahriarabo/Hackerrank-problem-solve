# Read input
n = int(input( ))
elements = input().split()

# Convert elements to integers and create the tuple
tuple_elements = tuple(map(int, elements))

# Calculate and print the hash of the tuple
tuple_hash = hash(tuple_elements)
print(tuple_hash)
