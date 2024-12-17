def is_palindrome(x):
    # Convert the integer to a string
    str_x = str(x)
    
    # Check if the string is equal to its reverse
    return str_x == str_x[::-1]

def main():
    # Input from the user
    try:
        x = int(input("Enter an integer: "))
        
        # Check if the integer is a palindrome
        if is_palindrome(x):
            print(f"{x} is a palindrome.")
        else:
            print(f"{x} is not a palindrome.")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
