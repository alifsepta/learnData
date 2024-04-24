class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        # Joining the strings in each list and checking if they are equal
        return ''.join(word1) == ''.join(word2)

solution = Solution()
print(solution.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))
print(solution.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))
print(solution.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))
