class Solution(object):
    def balancedStringSplit(self, s):
        count = 0  # Initialize a counter to keep track of balanced strings
        balance = 0  # Initialize a balance counter to track the number of 'L' and 'R'

        # Iterate over each character in the string
        for char in s:
            # Increment the balance counter if the character is 'L'
            if char == 'L':
                balance += 1
            # Decrement the balance counter if the character is 'R'
            else:
                balance -= 1

            # If the balance counter is zero, it means we have a balanced substring
            if balance == 0:
                count += 1  # Increment the balanced string count

        return count  # Return the number of balanced strings

# Create an instance of the Solution class
solution = Solution()

# Test the function with example inputs and print the outputs
print(solution.balancedStringSplit("RLRRLLRLRL"))  # Output: 4
print(solution.balancedStringSplit("RLRRRLLRLL"))  # Output: 2
print(solution.balancedStringSplit("LLLLRRRR"))    # Output: 1
