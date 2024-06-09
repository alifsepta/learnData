class Solution(object):
    def countPrefixSuffixPairs(self, words):
        # Define a helper function to check if a string is both a prefix and a suffix of another string
        def isPrefixAndSuffix(str1, str2):
            # Check if str1 is both a prefix and a suffix of str2
            return str2.startswith(str1) and str2.endswith(str1)
        
        # Initialize a variable to store the count of valid index pairs
        count = 0
        
        # Iterate through all index pairs (i, j), such that i < j
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                # Check if words[i] is a prefix and suffix of words[j]
                if isPrefixAndSuffix(words[i], words[j]):
                    # If yes, increment the count of valid index pairs
                    count += 1
        
        # Return the count of valid index pairs
        return count

# Instantiate the Solution class
solution = Solution()

# Example 1
words1 = ["a","aba","ababa","aa"]
output1 = solution.countPrefixSuffixPairs(words1)
print("Example 1 Output:", output1)  # Output: 4

# Example 2
words2 = ["pa","papa","ma","mama"]
output2 = solution.countPrefixSuffixPairs(words2)
print("Example 2 Output:", output2)  # Output: 2

# Example 3
words3 = ["abab","ab"]
output3 = solution.countPrefixSuffixPairs(words3)
print("Example 3 Output:", output3)  # Output: 0
