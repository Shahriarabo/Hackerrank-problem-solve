from itertools import product

def cartesian_product(A, B):
    # Compute the cartesian product using itertools.product
    product_result = list(product(A, B))
    
    # Print the tuples in sorted order
    for item in product_result:
        print(item, end=' ')

# Take input from the user
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Output the cartesian product of A and B
cartesian_product(A, B)
