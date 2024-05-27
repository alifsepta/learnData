class Solution(object):
    def prefixCount(self, words, pref):
        # Initialize a count variable to store the number of strings containing the prefix
        count = 0
        
        # Iterate through each word in the list of words
        for word in words:
            # Check if the current word starts with the prefix
            if word.startswith(pref):
                # If it does, increment the count
                count += 1
        
        # Return the final count
        return count

# Define the list of words and the prefix
words1 = ["pay", "attention", "practice", "attend"]
pref1 = "at"

# Create an instance of the Solution class
sol = Solution()

# Call the prefixCount method with the given inputs for the first example
output1 = sol.prefixCount(words1, pref1)

# Print the output for the first example
print("Output for Example 1:", output1)

# Define the list of words and the prefix for the second example
words2 = ["leetcode", "win", "loops", "success"]
pref2 = "code"

# Call the prefixCount method with the given inputs for the second example
output2 = sol.prefixCount(words2, pref2)

# Print the output for the second example
print("Output for Example 2:", output2)
