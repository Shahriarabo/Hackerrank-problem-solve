def check_string_properties(s):
    # Check if the string has any alphanumeric characters
    print(any(char.isalnum() for char in s))
    # Check if the string has any alphabetical characters
    print(any(char.isalpha() for char in s))
    # Check if the string has any digits
    print(any(char.isdigit() for char in s))
    # Check if the string has any lowercase characters
    print(any(char.islower() for char in s))
    # Check if the string has any uppercase characters
    print(any(char.isupper() for char in s))

if __name__ == "__main__":
    # Read the input string from the user
    input_string = input().strip()
    check_string_properties(input_string)

