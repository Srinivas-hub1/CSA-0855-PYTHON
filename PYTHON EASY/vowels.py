def count_vowels(input_string):
    # Define vowels
    vowels = "aeiouAEIOU"
    # Count vowels in the string
    count = sum(1 for char in input_string if char in vowels)
    return count

# Input
input_string = input("Enter a string: ")

# Count and display the number of vowels
num_vowels = count_vowels(input_string)
print("Number of vowels =", num_vowels)
