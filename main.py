"""
Arwin Ramesan
rame9880@mylaurier.ca
200619880
February 11, 2024
"""

matrix_a = [[6, 9], [2, 4], [3, 5]]
matrix_b = [[8, 1], [7, 3]]

def map_matrix_a(matrix, k_max):
    """
    Create key-value pairs of matrix A
    Params:
        matrix = integer list
        k_max = number of columns in matrix B
    Return:
        result = dictionary
                    key = coordinates
                    items = mapped values
    """
    result = {}
    i = 0
    for row in matrix:
        j = 0
        for col in row:
            for k in range(k_max):
                if str([i, k]) not in result.keys():
                    result[str([i, k])] = []
                
                # follows formula => (i, k) = (A, j, Aij)
                result[str([i, k])].append(["A", j, matrix[i][j]])
            j += 1
        i += 1
    return result

def map_matrix_b(matrix, k_max):
    """
    Create key-value pairs of matrix B
    Params:
        matrix = integer list
        k_max = number of rows in matrix A
    Return:
        result = dictionary
                    keys = coordinates
                    items = mapped values
    """
    result = {}
    i = 0
    for row in matrix:
        j = 0
        for col in row:
            for k in range(k_max):
                if str([k, j]) not in result.keys():
                    result[str([k, j])] = []
                
                # follows formula => (k, j) = (B, i, Bij)
                result[str([k, j])].append(["B", i, matrix[i][j]])

            j += 1
        i += 1
    return result

def combine(map_a, map_b):
    """
    Combines both key-value pair matrices of A and B
    """
    result = {}
    # each key is a coordinate
    for key in map_a.keys():
        result[key] = []
        for x in range(len(map_a[key])):
            # Append in alternating order so it is sorted in correct order for Reducing
            result[key].append(map_a[key][x])
            result[key].append(map_b[key][x])

    return result

def reduce(combined_matrix):
    """
    Calculates values for each coordinate
    """
    result = {}
    # each key is a coordinate
    keys = combined_matrix.keys()
    for key in keys:
        curr_sum = 0
        for n in range(0, len(combined_matrix[key]), 2):
            # Value to multiply is always the next value and only multiplies once, hence the increment of 2 in for loop to skip already multiplied value
            curr_sum += combined_matrix[key][n][2] * combined_matrix[key][n+1][2]
                
        result[key] = curr_sum

    return result

def printMatrix(matrix):
    # Outputs matrix with line breaks and coordinates
    for key in matrix:
        print(f"{key}: {matrix[key]}")

# Mapping
if len(matrix_a[0]) != len(matrix_b):
        print("Multiplication failed. Columns in matrix A don't match Rows in matrix B.")
else:
    result_a = map_matrix_a(matrix_a, len(matrix_b[0]))
    print("Mapping of Matrix A:")
    printMatrix(result_a)
    print('~'*50)
    result_b = map_matrix_b(matrix_b, len(matrix_a))
    print(f"Mapping of Matrix B:")
    printMatrix(result_b)
    print('~'*50)
    # Combining
    combined_result = combine(result_a, result_b)
    print(f"Combined and Ordered:")
    printMatrix(combined_result)
    print('~'*50)
    # Reducing
    reduce_result = reduce(combined_result)
    print(f"Reduced:")
    printMatrix(reduce_result)
