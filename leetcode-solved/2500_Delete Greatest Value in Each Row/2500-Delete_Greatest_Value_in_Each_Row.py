class Solution(object):
    def deleteGreatestValue(self, grid):
        # Initialize a variable to store the result
        result = 0
        
        # Initialize a list to keep track of visited cells
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        
        # Continue looping until all cells are visited
        while not all(all(row) for row in visited):
            # Initialize a list to store the maximum values in each row
            max_values = []
            
            # Iterate through each row
            for i in range(len(grid)):
                max_val = 0
                max_index = -1
                
                # Find the maximum unvisited value in the row
                for j in range(len(grid[i])):
                    if not visited[i][j] and grid[i][j] > max_val:
                        max_val = grid[i][j]
                        max_index = j
                
                # Mark the maximum value as visited
                if max_index != -1:
                    visited[i][max_index] = True
                    max_values.append(max_val)
            
            # Add the maximum value from the max_values list to the result
            result += max(max_values)
        
        # Return the final result
        return result

# Test the function with Example 1
grid1 = [[1,2,4],[3,3,1]]
solution = Solution()
print(solution.deleteGreatestValue(grid1))  # Output should be 8

# Test the function with Example 2
grid2 = [[10]]
print(solution.deleteGreatestValue(grid2))  # Output should be 10
