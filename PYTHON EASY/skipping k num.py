def print_numbers(M, N, K):
    # Iterate from M to N, stepping by K + 1 to skip K numbers
    for number in range(M, N + 1, K + 1):
        print(number, end=' ')
    print()  # For a new line after printing all numbers

def main():
    try:
        # Input from the user
        M = int(input("Enter the starting number (M): "))
        N = int(input("Enter the ending number (N): "))
        K = int(input("Enter the number of skips (K): "))
        
        # Print the numbers from M to N skipping K numbers
        print(f"Numbers from {M} to {N} skipping {K} numbers in between:")
        print_numbers(M, N, K)
    
    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
