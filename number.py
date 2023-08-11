def print_formatted(number):
    width = len(bin(number)[2:])  # Calculate the width based on the binary representation

    for i in range(1, number + 1):
        decimal_str = str(i).rjust(width)  # Right-justify the decimal representation
        octal_str = oct(i)[2:].rjust(width)  # Remove the '0o' prefix and right-justify the octal representation
        hex_str = hex(i)[2:].upper().rjust(width)  # Remove the '0x' prefix, capitalize, and right-justify the hex representation
        binary_str = bin(i)[2:].rjust(width)  # Remove the '0b' prefix and right-justify the binary representation

        print(f"{decimal_str} {octal_str} {hex_str} {binary_str}")

# Test with the given sample input
if __name__ == "__main__":
    number = 17
    print_formatted(number)
