def factorial():
    try:
        n = input("Enter N: ").strip()
        
        # Check if input is a valid integer
        if not n.isdigit() and not (n.startswith('-') and n[1:].isdigit()):
            print(f"N = {n} is invalid. Please enter a valid integer.")
            return
        
        n = int(n)
        
        # Handle negative input
        if n < 0:
            print(f"Factorial of negative numbers is not defined. N = {n} is invalid.")
            return
        
        # Calculate factorial
        result = 1
        for i in range(1, n + 1):
            result *= i
        
        print(f"{n} Factorial = {result}")
    
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Test the function
factorial()
