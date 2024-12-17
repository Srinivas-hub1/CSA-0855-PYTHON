def add_matrices(matrix1, matrix2):
    # Check if the dimensions of the matrices are the same
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    
    # Create a new matrix to store the result
    result = []
    
    # Iterate through the rows
    for i in range(len(matrix1)):
        # Create a new row for the result
        row = []
        # Iterate through the columns
        for j in range(len(matrix1[0])):
            # Add corresponding elements
            row.append(matrix1[i][j] + matrix2[i][j])
        # Append the row to the ⬤
