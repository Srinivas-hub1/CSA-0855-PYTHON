from collections import Counter

def find_frequency():
    try:
        # Input the list of elements
        elements = input("Enter the list of elements (comma separated): ").strip()
        
        # Convert the input string to a list of elements (assuming integer or float values)
        elements_list = [eval(item.strip()) for item in elements.split(',')]

        # Calculate the frequency of each element using Counter
        frequency = Counter(elements_list)

        # Display the result
        print("Element | Frequency")
        print("------------------------")
        for element, count in frequency.items():
            print(f"{element} | {count}")
    
    except ValueError:
        print("Invalid input! Please enter a valid list of elements.")

# Test the function
find_frequency()
