class Solution(object):
    def countConsistentStrings(self, allowed, words):
        # Initialize a counter to store the count of consistent strings
        count = 0
        
        # Create a set of characters allowed for faster lookup
        allowed_set = set(allowed)
        
        # Iterate through each word in the list of words
        for word in words:
            # Assume the word is consistent initially
            consistent = True
            # Check each character in the word
            for char in word:
                # If the character is not in the set of allowed characters,
                # mark the word as inconsistent and break the loop
                if char not in allowed_set:
                    consistent = False
                    break
            # If the word is consistent, increment the count
            if consistent:
                count += 1
        
        # Return the count of consistent strings
        return count

# Example usage:
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
solution = Solution()
print(solution.countConsistentStrings(allowed, words))  # Output: 2
