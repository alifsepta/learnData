class Solution(object):
    def restoreString(self, s, indices):
        # Create a list of the same length as the string
        shuffled = [None] * len(s)
        
        # Iterate through each character in the string s and its corresponding index
        for i, char in zip(indices, s):
            # Place the character at its corresponding index in the shuffled list
            shuffled[i] = char
        
        # Join the characters in the shuffled list to form the shuffled string
        return ''.join(shuffled)

solution = Solution()
# Test cases
print(solution.restoreString("codeleet", [4,5,6,7,0,2,1,3]))  # Output: "leetcode"
print(solution.restoreString("abc", [0,1,2]))  # Output: "abc"
