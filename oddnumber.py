# Program to print odd numbers from 1 to 100

def print_odd_numbers(start: int, end: int):
    """
    Prints all odd numbers between start and end (inclusive).
    """
    # Ensure start <= end
    if start > end:
        start, end = end, start

    for num in range(start, end + 1):
        if num % 2 != 0:  # Check if number is odd
            print(num, end=" ")
    print()  # Newline after printing all numbers


if __name__ == "__main__":
    try:
        # Fixed range 1 to 100 as per requirement
        print("Odd numbers from 1 to 100:")
        print_odd_numbers(1, 100)
    except Exception as e:
        print(f"An error occurred: {e}")
