def calculate_simple_interest(principal, years, is_senior_citizen):
    # Determine the rate of interest based on senior citizen status
    if is_senior_citizen:
        rate_of_interest = 12  # 12% for senior citizens
    else:
        rate_of_interest = 10  # 10% for others
    
    # Calculate simple interest
    interest = (principal * rate_of_interest * years) / 100
    return interest

def main():
    try:
        # Input from the user
        principal = float(input("Enter the principal amount: "))
        years = float(input("Enter the number of years: "))
        senior_citizen_input = input("Is the customer a senior citizen (y/n): ").strip().lower()
        
        # Validate senior citizen input
        if senior_citizen_input not in ['y', 'n']:
            print("Invalid input for senior citizen status. Please enter 'y' or 'n'.")
            return
        
        # Determine if the customer is a senior citizen
        is_senior_citizen = senior_citizen_input == 'y'
        
        # Validate principal and years
        if principal < 0 or years < 0:
            print("Principal and years must be non-negative.")
            return
        
        # Calculate interest
        interest = calculate_simple_interest(principal, years, is_senior_citizen)
        
        # Output the result
        print(f"Interest: {interest}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for principal and years.")

if __name__ == "__main__":
    main()
