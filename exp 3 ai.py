# Define a matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Transpose the matrix
transpose = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        transpose[j][i] = matrix[i][j]

# Print the transposed matrix
print("Transposed Matrix:")
for row in transpose:
    print(row)
