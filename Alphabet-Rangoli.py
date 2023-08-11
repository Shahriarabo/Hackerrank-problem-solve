def print_rangoli(n):
    import string

    # Create the alphabet string from a to z using string.ascii_lowercase
    alphabet = string.ascii_lowercase

    # Create a list to store each line of the rangoli
    rangoli_lines = []

    # Build the rangoli
    for i in range(n - 1, -n, -1):
        # Get the characters for the current line
        line = '-'.join(alphabet[n-1:abs(i):-1] + alphabet[abs(i):n])
        rangoli_lines.append(line.center(4*n - 3, '-'))

    # Print the rangoli
    print('\n'.join(rangoli_lines))





if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
