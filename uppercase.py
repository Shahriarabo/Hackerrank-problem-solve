name = input()
n= name.upper()
m = name.lower()
print(format(name.swapcase()))

def swap_case(s):
    return s.swapcase()

# Test the function with the provided sample input
sample_input = 'HackerRank.com presents "Pythonist 2".'
result = swap_case(sample_input)
print(result)
