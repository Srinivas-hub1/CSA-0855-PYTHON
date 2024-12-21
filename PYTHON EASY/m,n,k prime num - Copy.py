def print_numbers(M, N, K):
    # Check for valid input where M should be less than N
    if M > N:
        print("Invalid range: M should be less than N.")
        return
    
    numbers = []
    
    # Generate the numbers from M to N, skipping K numbers in between
    while M <= N:
        numbers.append(M)
        M += K + 1  # Skip K numbers and move to the next number
        
    return numbers

def main():
    try:
        # Input M, N, and K from the user
        M = int(input("Enter the value of M: "))
        N = int(input("Enter the value of N: "))
        K = int(input("Enter the value of K: "))
        
        # Get the list of numbers
        result = print_numbers(M, N, K)
        
        # Print the result
        if result:
            print(", ".join(map(str, result)))
        
    except ValueError:
        print("Invalid input! Please enter valid integers.")

# Test the function
main()


