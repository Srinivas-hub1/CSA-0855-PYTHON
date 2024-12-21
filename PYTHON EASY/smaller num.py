def smaller_numbers_than_current(nums):
    # Initialize the result list
    result = []
    
    # Iterate through each number in the list
    for i in range(len(nums)):
        count = 0
        # Compare the current number with all other numbers in the list
        for j in range(len(nums)):
            if j != i and nums[j] < nums[i]:
                count += 1
        # Append the count to the result list
        result.append(count)
    
    return result

def main():
    try:
        # Input the list of numbers
        nums = list(map(int, input("Enter the numbers separated by spaces: ").split()))
        # Call the function and print the result
        print("Output:", smaller_numbers_than_current(nums))
    except ValueError:
        print("Invalid input! Please enter a list of integers.")

# Run the program
main()
