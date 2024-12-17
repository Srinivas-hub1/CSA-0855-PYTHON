def print_pattern(rows):
    for i in range(1, rows + 1):
        # Print numbers from i down to 1
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()  # Move to the next line after each row

def main():
    try:
        # Input from the user
        rows = int(input("Number of rows: "))
        
        # Print the pattern
        print_pattern(rows)
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
