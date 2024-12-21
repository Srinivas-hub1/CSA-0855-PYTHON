def reverse_number():
    try:
        # Input the number as a string
        num = input("Enter the number: ").strip()

        # Validate input
        if not num.lstrip('-').isdigit():
            print(f"'{num}' is not a valid number.")
            return

        # Reverse the number using a loop
        reversed_num = ""
        for digit in reversed(num):
            reversed_num += digit

        # Handle negative numbers
        if num.startswith('-'):
            reversed_num = '-' + reversed_num.rstrip('-')

        print(f"Reverse Number: {reversed_num}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Test the function
reverse_number()
