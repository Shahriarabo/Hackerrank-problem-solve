def merge_the_tools(s, k):
    n = len(s)
    num_substrings = n // k

    for i in range(num_substrings):
        substring = s[i * k : (i + 1) * k]
        unique_chars = []
        for char in substring:
            if char not in unique_chars:
                unique_chars.append(char)
        print("".join(unique_chars))




if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
