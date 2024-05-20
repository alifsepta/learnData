class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        # Initialize a counter variable to keep track of the number of jewels found
        count = 0
        
        # Iterate through each stone in the stones string
        for stone in stones:
            # Check if the stone is in the jewels string
            if stone in jewels:
                # If the stone is a jewel, increment the count
                count += 1
        
        # Return the total count of jewels found in the stones
        return count

# Example 1
jewels1 = "aA"
stones1 = "aAAbbbb"
# Create an instance of the Solution class
sol = Solution()
# Call the numJewelsInStones method with the given inputs
output1 = sol.numJewelsInStones(jewels1, stones1)
# Print the output
print("Example 1 Output:", output1)

# Example 2
jewels2 = "z"
stones2 = "ZZ"
# Call the numJewelsInStones method with the given inputs
output2 = sol.numJewelsInStones(jewels2, stones2)
# Print the output
print("Example 2 Output:", output2)
