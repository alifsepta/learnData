class Solution(object):
    def diagonalSum(self, mat):
        n = len(mat)  # Get the size of the square matrix (number of rows/columns)
        primary_sum = 0  # Initialize the sum of elements on the primary diagonal
        secondary_sum = 0  # Initialize the sum of elements on the secondary diagonal

        for i in range(n):
            primary_sum += mat[i][i]  # Add the element on the primary diagonal
            secondary_sum += mat[i][n - i - 1]  # Add the element on the secondary diagonal
            
        # If the matrix size is odd, the center element is counted twice, so subtract it once
        if n % 2 == 1:
            primary_sum -= mat[n // 2][n // 2]

        return primary_sum + secondary_sum  # Return the sum of both diagonals

# Create an instance of the Solution class
solution = Solution()

# Test cases
mat1 = [[1,2,3], [4,5,6], [7,8,9]]
print(solution.diagonalSum(mat1))  # Output: 25

mat2 = [[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]
print(solution.diagonalSum(mat2))  # Output: 8

mat3 = [[5]]
print(solution.diagonalSum(mat3))  # Output: 5
