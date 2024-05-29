class Solution(object):
    def countNegatives(self, grid):
        # Initialize a variable to store the count of negative numbers
        count = 0
        
        # Iterate through each row in the grid
        for row in grid:
            # Iterate through each element in the row
            for num in row:
                # If the number is negative, increment the count
                if num < 0:
                    count += 1
        
        # Return the count of negative numbers
        return count

# Instantiate the Solution class
sol = Solution()

# Test cases
grid1 = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
grid2 = [[3,2],[1,0]]

# Print the output for each test case
print("Output for grid1:", sol.countNegatives(grid1))
print("Output for grid2:", sol.countNegatives(grid2))
