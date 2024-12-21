def nth_odd_after_n_odds():
    try:
        n = float(input("Enter N: "))
        
        # Ensure n is a valid integer
        if not n.is_integer():
            print(f"N = {n} is not a valid integer.")
            return
        
        n = int(n)  # Convert to integer
        
        if n < 0:
            print(f"N = {n} is invalid. Please enter a non-negative integer.")
            return
        
        # Calculate the n-th odd number after n odd numbers
        # Formula for n-th odd number: 2n - 1
        nth_odd = 2 * n - 1
        nth_odd_after_n = nth_odd + 2 * n
        print(f"{n}th odd number after {n} odd numbers = {nth_odd_after_n}")
    
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Test the function
nth_odd_after_n_odds()
