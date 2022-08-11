# return a 2D matrix of popped 'firecrackers'

# Instead of making a second matrix, save memory by directly changing inputted matrix
# change only the first row and col to zero initially, then use that as references to make all following edits

def explodeFirecrackers(matrix):
    # variables to get matrix dimensions
    ROWS = len(matrix)
    COLS = len(matrix[0])
    setTopRow = False

    # mark all required first row and col with zero
    for row in range(ROWS):
        for col in range(COLS):
            # find all zeros
            if matrix[row][col] == 0:
                # wherever zero is found, mark first row's column
                matrix[0][col] = 0
                # if on first row, set flag so that there is no interference between (0,0) cell in matrix throwing off results
                if row == 0:
                    setTopRow = True
                # if not, make the first column zero
                else:
                    matrix[row][0] = 0
                
    
    # then make changes to rest of matrix, now ignoring the first row and column
    for row in range(1, ROWS):
        for col in range(1, COLS):
            if matrix[row][0] == 0 or matrix[0][col] == 0:
                matrix[row][col] = 0
   
   # flag ensures that top row is fully zeroed out, not just columns with zeros found
    if setTopRow:
        for col in range(COLS):
            matrix[0][col] = 0
        
    # if (0,0) is zero, change the first column entirely
    if matrix[0][0] == 0:
        for row in range(ROWS):
            matrix[row][0] = 0
    
    return matrix        

# Given Test

matrix1 = [
    [5, 0, 0, 5, 8],
    [9, 8, 10, 3, 9],
    [0, 7, 2, 3, 1],
    [8, 0, 6, 7, 2],
    [4, 1, 8, 5, 10]
]

print(explodeFirecrackers(matrix1))

# Made up tests

matrix2 = [
    [0, 6, 4, 5, 8],
    [9, 8, 4, 0, 9],
    [7, 7, 2, 3, 1],
    [8, 8, 6, 7, 2],
    [4, 1, 0, 5, 10]
]

print(explodeFirecrackers(matrix2))

exit()