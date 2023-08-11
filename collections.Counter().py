from collections import Counter

def calculate_earnings(shoe_count, shoe_sizes, customer_count, customer_data):
    shoe_inventory = Counter(shoe_sizes)
    total_earnings = 0
    
    for i in range(customer_count):
        size, price = customer_data[i]
        if shoe_inventory[size] > 0:
            total_earnings += price
            shoe_inventory[size] -= 1
            
    return total_earnings

# Read input
shoe_count = int(input())
shoe_sizes = list(map(int, input().split()))
customer_count = int(input())
customer_data = [list(map(int, input().split())) for _ in range(customer_count)]

# Calculate and print the earnings
earnings = calculate_earnings(shoe_count, shoe_sizes, customer_count, customer_data)
print(earnings)
