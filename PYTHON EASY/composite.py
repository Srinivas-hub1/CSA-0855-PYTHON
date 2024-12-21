def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_prime_and_composite(numbers):
    prime_count = 0
    composite_count = 0

    for num in numbers:
        if num > 1:  # Only consider numbers greater than 1 for prime/composite
            if is_prime(num):
                prime_count += 1
            else:
                composite_count += 1
    return prime_count, composite_count

# Main program
try:
    input_numbers = input("Enter the numbers: ").split()
    numbers = []

    # Validate and parse input
    for num in input_numbers:
        try:
            parsed_num = float(num)
            if parsed_num.is_integer():
                numbers.append(int(parsed_num))
        except ValueError:
            continue  # Ignore invalid inputs (e.g., text or special characters)

    # Count primes and composites
    prime_count, composite_count = count_prime_and_composite(numbers)

    print(f"Composite numbers: {composite_count}")
    print(f"Prime numbers: {prime_count}")

except Exception as e:
    print(f"An error occurred: {e}")
