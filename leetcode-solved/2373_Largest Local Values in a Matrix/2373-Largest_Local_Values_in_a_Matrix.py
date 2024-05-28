def generate_max_local(grid):
    n = len(grid)
    max_local = []
    
    # Iterate through the rows (except the first and last 2 rows)
    for i in range(1, n - 1):
        row_max = []
        # Iterate through the columns (except the first and last 2 columns)
        for j in range(1, n - 1):
            # Find the maximum value in the 3x3 submatrix centered at grid[i][j]
            max_value = max(
                grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1],
                grid[i][j - 1],     grid[i][j],     grid[i][j + 1],
                grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1]
            )
            row_max.append(max_value)
        max_local.append(row_max)
    
    return max_local

# Example 1
grid1 = [
    [9, 9, 8, 1],
    [5, 6, 2, 6],
    [8, 2, 6, 4],
    [6, 2, 2, 2]
]

max_local1 = generate_max_local(grid1)
print("Output for Example 1:", max_local1)

# Example 2
grid2 = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]

max_local2 = generate_max_local(grid2)
print("Output for Example 2:", max_local2)
