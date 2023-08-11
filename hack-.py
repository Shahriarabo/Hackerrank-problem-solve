def split_and_join(line):
    # Split the input string on space delimiter and store the words in a list
    words = line.split(" ")
    
    # Join the words using hyphen (-) as the separator
    result = "-".join(words)
    
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
