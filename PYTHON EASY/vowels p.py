def count_vowels(input_string):
    # Define the set of vowels (both lowercase and uppercase)
    vowels = "aeiouAEIOU"
    
    # Initialize a count variable
    count = 0
    
    # Iterate over each character in the string
    for char in input_string:
        # Check if the character is a vowel
        if char in vowels:
            count += 1
    
    return count

# Test cases
test_cases = [
    "India is my country", 
    "All are my brothers and sisters", 
    "Why dry sky", 
    "Shy Try Cry", 
    "EDUCATION"
]

for case in test_cases:
    print(f"Input: {case}")
    print(f"Number of vowels = {count_vowels(case)}\n")
