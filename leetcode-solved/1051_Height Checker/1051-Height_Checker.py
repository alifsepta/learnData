class Solution(object):
    def heightChecker(self, heights):
        # Create a sorted version of the expected heights array
        expected = sorted(heights)
        # Initialize a variable to count the number of indices where heights != expected
        count = 0
        
        # Iterate over the indices of the heights array
        for i in range(len(heights)):
            # If the height at the current index in heights is not equal to the expected height at the same index
            if heights[i] != expected[i]:
                # Increment the count
                count += 1
        
        # Print the output
        print("Output:", count)
        # Return the count
        return count

# Test cases
solution = Solution()
print("Test Case 1:")
print("Input:", [1, 1, 4, 2, 1, 3])
solution.heightChecker([1, 1, 4, 2, 1, 3])

print("\nTest Case 2:")
print("Input:", [5, 1, 2, 3, 4])
solution.heightChecker([5, 1, 2, 3, 4])

print("\nTest Case 3:")
print("Input:", [1, 2, 3, 4, 5])
solution.heightChecker([1, 2, 3, 4, 5])
