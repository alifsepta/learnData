class Solution(object):
    def cellsInRange(self, s):
        # Extract col1, row1, col2, row2 from the input string
        col1, row1, col2, row2 = s[0], int(s[1]), s[3], int(s[4])
        
        # Initialize an empty list to store the cells
        cells = []
        
        # Iterate through the columns in ascending order
        for col in range(ord(col1), ord(col2) + 1):
            # Iterate through the rows in ascending order
            for row in range(row1, row2 + 1):
                # Construct the cell representation and append it to the list
                cells.append(chr(col) + str(row))
        
        # Sort the list of cells
        cells.sort()
        
        # Return the sorted list of cells
        return cells

# Instantiate the Solution class
solution = Solution()

# Test cases
test_cases = ["K1:L2", "A1:F1"]

# Loop through each test case
for test in test_cases:
    # Call the cellsInRange method and print the output
    print(solution.cellsInRange(test))
