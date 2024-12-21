'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
'''
# Path to your input file
file_path = 'input07.txt'

# Read the entire content of the file into a variable
with open(file_path, 'r') as file:
    data = file.read()

# Split the data by newlines to get individual lines
lines = data.strip().split('\n')

# Parse the first line to get the size of the matrix
n = int(lines[0].strip())

# Initialize an empty list to store the rows of the matrix
arr = []

# Iterate over the remaining lines and parse each row into integers
for line in lines[1:]:
    arr.append(list(map(int, line.split())))

def diagonalDifference(arr):
    n = len(arr)
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0

    # Calculate the primary diagonal
    for i in range(n):
        primary_diagonal_sum += arr[i][i]
    print(f"Sum of primany Diagonal is{primary_diagonal_sum} ")

    # Calculate the secondary diagonal
    for i in range(n):
        secondary_diagonal_sum += arr[i][n - i - 1]
    print(f"Sum of secondary Diagonal is{secondary_diagonal_sum} ")

    return abs(primary_diagonal_sum - secondary_diagonal_sum)

# Call the function and print the result
result = diagonalDifference(arr)
print(f'Absolute Difference between both the diagonals is {result}')