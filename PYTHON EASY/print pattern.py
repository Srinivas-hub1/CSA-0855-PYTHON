def print_pattern():
    try:
        # Input character and maximum number of times
        char = input("Enter the character to be printed: ").strip()
        max_times = int(input("Max number of times printed: ").strip())
        
        # Validate inputs
        if len(char) != 1:
            print(f"'{char}' is invalid. Please enter a single character.")
            return
        
        if max_times < 0:
            print(f"Max number of times printed ({max_times}) is invalid. Please enter a non-negative integer.")
            return
        
        # Print the pattern
        for i in range(1, max_times + 1):
            print(char * i)
    
    except ValueError:
        print("Invalid input! Please enter valid inputs.")

# Test the function
print_pattern()
