import math

def count_common_divisors(a, b):
    # Calculate the GCD of the two numbers
    gcd = math.gcd(a, b)
    
    # Count the divisors of the GCD
    divisors_count = 0
    for i in range(1, int(math.sqrt(gcd)) + 1):
        if gcd % i == 0:
            # Count both i and gcd // i if they are distinct
            if i == gcd // i:
                divisors_count += 1
            else:
                divisors_count += 2
    return divisors_count

def main():
    # Get input from the user
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        if num1 == 0 and num2 == 0:
            print("Output: Undefined (0 and 0 have infinite divisors in common)")
        else:
            result = count_common_divisors(num1, num2)
            print("Output:", result)
    except ValueError:
        print("Invalid input. Please enter integers only.")

# Run the program
main()
