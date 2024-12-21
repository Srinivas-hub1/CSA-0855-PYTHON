from statistics import mean, median, mode, StatisticsError

def calculate_mean_median_mode():
    try:
        # Input the list of elements
        elements = input("Enter the list of elements separated by spaces: ").strip().split()
        
        # Convert input strings to numbers
        elements = [float(num) for num in elements]
        
        # Calculate Mean
        mean_value = mean(elements)
        
        # Calculate Median
        median_value = median(elements)
        
        # Calculate Mode (handle cases where mode may not exist)
        try:
            mode_value = mode(elements)
        except StatisticsError:
            mode_value = "No unique mode"
        
        # Display results
        print(f"Mean = {mean_value:.2f}")
        print(f"Median = {median_value:.2f}")
        print(f"Mode = {mode_value}")
    
    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Test the function
calculate_mean_median_mode()
