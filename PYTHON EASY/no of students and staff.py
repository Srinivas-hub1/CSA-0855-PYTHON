def main():
    # Get the number of student users
    try:
        num_students = int(input("Enter the number of student users in the college: "))
        
        # Get the total number of users
        total_users = int(input("Enter the total number of users in the college: "))
        
        # Calculate the number of staff users
        num_staff_users = total_users - num_students
        
        # Calculate the number of non-teaching staff users
        num_non_teaching_staff = num_staff_users // 3
        
        # Get details of staff users
        staff_details = []
        for i in range(num_staff_users):
            staff_name = input(f"Enter the name of staff user {i + 1}: ")
            staff_role = input(f"Enter the role of staff user {i + 1}: ")
            staff_details.append((staff_name, staff_role))
        
        # Print the results
        print("\nSummary:")
        print(f"Number of student users: {num_students}")
        print(f"Total number of users: {total_users}")
        print(f"Number of staff users: {num_staff_users}")
        print(f"Number of non-teaching staff users: {num_non_teaching_staff}")
        
        print("\nStaff User Details:")
        for i, (name, role) in enumerate(staff_details):
            print(f"Staff User {i + 1}: Name: {name}, Role: {role}")
    
    except ValueError:
        print("Please enter valid integer values.")

if __name__ == "__main__":
    main()
