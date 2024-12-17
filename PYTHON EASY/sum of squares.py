def sumsquare(l):
    # Initialize sums for odd and even squares
    odd_sum = 0
    even_sum = 0
    
    # Iterate through each number in the list
    for number in l:
        if number % 2 == 0:  # Check if the number is even
            even_sum += number ** 2  # Add square of even number
        else:  # The number is odd
            odd_sum += number ** 2  # Add square of odd number
    
    # Return the results as a list [odd_sum, even_sum]
    return [odd_sum, even_sum]

# Example usage
if __name__ == "__main__":
    # Test the function with a sample list
    sample_list = [1, 2, 3, 4, 5]
    result = sumsquare(sample_list)
    print(f"Sum of squares: {result}")  # Output: [35, 20]
