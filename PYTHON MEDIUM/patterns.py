def print_pattern(start, lines):
    if lines < 1:  # Check for invalid line count
        print("Number of lines must be a positive integer.")
        return

    current = start
    for i in range(1, lines + 1):  # i represents the number of values per line
        for j in range(i):
            print(f"{current:.1f}", end=" ")  # Print with 1 decimal place
            current += 0.1  # Increment by 0.1
        print()  # Move to the next line

# Input
try:
    start = float(input("Enter the starting number: "))
    lines = int(input("Max number of lines printed: "))

    # Print the pattern
    print_pattern(start, lines)
except ValueError:
    print("Invalid input! Please enter a valid number.")
