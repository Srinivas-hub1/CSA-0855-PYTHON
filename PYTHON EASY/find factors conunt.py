def find_factors_count(N):
    # Check for invalid input
    if not isinstance(N, int):
        print("Invalid input. Please enter a valid integer.")
        return
    
    # Handle special cases
    if N <= 0:
        print(f"Number of factors for {N}: Undefined for non-positive integers.")
        return
    
    # Count the factors
    count = 0
    for i in range(1, N + 1):
        if N % i == 0:
            count += 1
    print(f"Number of factors for {N}: {count}")

# Test Cases
print("Test Case 1:")
find_factors_count(0)

print("\nTest Case 2:")
find_factors_count(-5)

print("\nTest Case 3:")
find_factors_count(1)

print("\nTest Case 4:")
find_factors_count(20)

print("\nTest Case 5:")
find_factors_count("3A")
