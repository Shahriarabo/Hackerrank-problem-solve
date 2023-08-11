def mutate_string(s, position, character):
    # Convert the string to a list to make it mutable
    i = list(s)
    
    # Update the character at the given position
    i[position] = character
    
    # Convert the list back to a string and return the result
    return ''.join(i)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
