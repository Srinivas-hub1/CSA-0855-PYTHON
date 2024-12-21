def calculate_grade():
    try:
        # Input marks for four subjects
        python = float(input("Enter the marks in Python: "))
        c_programming = float(input("Enter the marks in C Programming: "))
        mathematics = float(input("Enter the marks in Mathematics: "))
        physics = float(input("Enter the marks in Physics: "))

        # Validate marks
        if any(m < 0 or m > 100 for m in [python, c_programming, mathematics, physics]):
            print("Invalid marks entered! Marks should be between 0 and 100.")
            return
        
        # Calculate total and aggregate
        total = python + c_programming + mathematics + physics
        aggregate = total / 4

        # Determine grade
        if aggregate > 75:
            grade = "Distinction"
        elif 60 <= aggregate < 75:
            grade = "First Division"
        elif 50 <= aggregate < 60:
            grade = "Second Division"
        elif 40 <= aggregate < 50:
            grade = "Third Division"
        else:
            grade = "Fail"

        # Display results
        print(f"Total: {total}")
        print(f"Aggregate: {aggregate:.2f}")
        print(f"Grade: {grade}")
    except ValueError:
        print("Invalid input! Please enter numeric values for marks.")

# Test the function with user input
calculate_grade()
