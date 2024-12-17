def sort_names(names, order):
    """Sorts the list of names in the specified order."""
    if order == 'ascending':
        return sorted(names)
    elif order == 'descending':
        return sorted(names, reverse=True)
    else:
        raise ValueError("Order must be 'ascending' or 'descending'.")

def main():
    # Get a list of names from the user
    names_input = input("Enter names separated by commas: ")
    names = [name.strip() for name in names_input.split(',')]
    
    # Get the sorting order from the user
    order = input("Enter sorting order (ascending/descending): ").strip().lower()
    
    try:
        # Sort the names based on user choice
        sorted_names = sort_names(names, order)
        
        # Print the sorted names
        print("Sorted names:")
        for name in sorted_names:
            print(name)
    
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
