def wrap(string, max_width):
    # Initialize an empty result string to store the wrapped text
    wrapped_text = ""

    # Loop through the string with steps of max_width
    for i in range(0, len(string), max_width):
        # Add a substring of length max_width to the result string
        wrapped_text += string[i:i + max_width] + '\n'

    return wrapped_text

# Test with the given sample input
if __name__ == "__main__":
    input_string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    width = 4
    result = wrap(input_string, width)
    print(result)
