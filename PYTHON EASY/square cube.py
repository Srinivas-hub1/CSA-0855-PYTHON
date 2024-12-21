def calculate_square_and_cube(number):
    # Calculate square and cube
    square = number ** 2
    cube = number ** 3
    
    # Print the results
    print(f"Square Number: {square}")
    print(f"Cube Number: {cube}")

def main():
    try:
        # Input from the user
        given_number = float(input("Given Number: "))
        # Call the function to calculate square and cube
        calculate_square_and_cube(given_number)
    except ValueError:
        print("Invalid input! Please enter a valid decimal number.")

# Run the program
main()
