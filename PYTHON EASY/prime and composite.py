def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes_and_composites():
    try:
        # Input numbers as a single string and split into a list
        numbers = input("Enter the numbers separated by spaces: ").strip().split()
        
        prime_count = 0
        composite_count = 0

        for num in numbers:
            # Validate if the input is a positive integer
            if not num.isdigit():
                print(f"'{num}' is invalid. Skipping.")
                continue
            
            num = int(num)
            
            if num <= 1:
                print(f"{num} is neither prime nor composite. Skipping.")
                continue
            
            # Count primes and composites
            if is_prime(num):
                prime_count += 1
            else:
                composite_count += 1
        
        print(f"Composite numbers: {composite_count}")
        print(f"Prime numbers: {prime_count}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Test the function
count_primes_and_composites()
