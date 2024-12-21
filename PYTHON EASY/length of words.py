def length_of_last_word(s):
    # Remove leading and trailing spaces and split the string into words
    words = s.strip().split()
    # Return the length of the last word
    return len(words[-1]) if words else 0

def main():
    # Get input from the user
    s = input("Enter the string: ")
    # Call the function and print the result
    print("Length of the last word:", length_of_last_word(s))

# Run the program
main()
