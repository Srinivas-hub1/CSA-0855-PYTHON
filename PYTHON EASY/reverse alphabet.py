def arrange_letters_reverse():
    word = input("Enter the word: ").strip().upper()  # Convert to uppercase for uniformity
    sorted_letters = sorted(word, reverse=True)  # Sort letters in reverse order
    result = " ".join(sorted_letters)
    print(f"Alphabetical Order: {result}")

# Test the function with user input
arrange_letters_reverse()
