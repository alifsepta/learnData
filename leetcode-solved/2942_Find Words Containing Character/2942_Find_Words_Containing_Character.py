class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        indices = []  # Initialize an empty list to store the indices
        
        # Iterate through each word in the list of words
        for i, word in enumerate(words):
            # Check if the character x is present in the current word
            if x in word:
                # If x is found, append the index of the word to the indices list
                indices.append(i)
        
        return indices

# Test cases
solution = Solution()
print(solution.findWordsContaining(["leet", "code"], "e"))   # Output: [0, 1]
print(solution.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "a"))   # Output: [0, 2]
print(solution.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "z"))   # Output: []
