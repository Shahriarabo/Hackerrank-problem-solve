def is_weird(n):

  if n % 2 == 1:
    return "Weird"

  if n >= 2 and n <= 5:
    return "Not Weird"

  if n >= 6 and n <= 20:
    return "Weird"

  return "Not Weird"


def main():
 
  n = int(input("Enter a number: "))

  print(is_weird(n))


if __name__ == "__main__":
  main()
