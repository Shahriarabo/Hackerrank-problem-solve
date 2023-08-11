def calculate_triangle_area(base, height):
    return 0.5 * base * height

def main():
    try:
        base, height = map(float, input().split())
        area = calculate_triangle_area(base, height)

        big_number = 1000  # Define the big number threshold

        if area > big_number:
            
            print(area)
        else:
            
            if area.is_integer():
                print(int(area))  # Print only the integer part if it's a whole number
            else:
                print(area)
    except ValueError:
        print("Invalid input. Please enter valid float numbers for the base and height.")

if __name__ == "__main__":
    main()
