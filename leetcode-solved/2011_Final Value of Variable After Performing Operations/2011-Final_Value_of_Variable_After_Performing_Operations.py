class Solution(object):
    def finalValueAfterOperations(self, operations):
        # Initialize variable to store the final value of X
        final_value = 0
        
        # Iterate through each operation in the list
        for operation in operations:
            # Check if the operation is either "--X" or "X--"
            if "--" in operation:
                # Decrement the value of X by 1
                final_value -= 1
            # Check if the operation is either "++X" or "X++"
            elif "++" in operation:
                # Increment the value of X by 1
                final_value += 1
        
        # Return the final value of X
        return final_value

# Create an instance of the Solution class
solution = Solution()

# Test cases
operations_1 = ["--X","X++","X++"]
operations_2 = ["++X","++X","X++"]
operations_3 = ["X++","++X","--X","X--"]

# Print the outputs for each test case
print(solution.finalValueAfterOperations(operations_1))  # Output: 1
print(solution.finalValueAfterOperations(operations_2))  # Output: 3
print(solution.finalValueAfterOperations(operations_3))  # Output: 0
