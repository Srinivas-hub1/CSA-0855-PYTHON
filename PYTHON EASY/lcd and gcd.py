

def find_gcd(a, b):
    return math.gcd(a, b)

def find_lcm(a, b):
    return abs(a * b) // find_gcd(a, b)

# Function to find the LCM and GCD of n numbers
def find_lcm_and_gcd_of_n_numbers():
    try:
        # Input the value of n (the number of elements)
        n = int(input("Enter the value of N: "))
        
        # Input the numbers in a list
        numbers = []
        for i in range(n):
            num = int(input(f"Enter number {i + 1}: "))
            numbers.append(num)

        if n < 2:
            print("You need at least two numbers to calculate LCM and GCD.")
            return
        
        # Initialize GCD and LCM with the first number
        gcd_result = numbers[0]
        lcm_result = numbers[0]

        # Loop through the remaining numbers and update the LCM and GCD
        for num in numbers[1:]:
            gcd_result = find_gcd(gcd_result, num)
            lcm_result = find_lcm(lcm_result, num)

        # Display the results
        print(f"LCM = {lcm_result}")
        print(f"GCD = {gcd_result}")

    except ValueError:
        print("Invalid input! Please enter integers.")

# Test the function
find_lcm_and_gcd_of_n_numbers()
