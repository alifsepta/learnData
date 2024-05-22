class Solution(object):
    def findPermutationDifference(self, s, t):
        permutation_diff = 0
        for char in s:
            index_s = s.index(char)  # Index of character in s
            index_t = t.index(char)  # Index of character in t
            permutation_diff += abs(index_s - index_t)
        return permutation_diff

# Example usage:
solution = Solution()
output1 = solution.findPermutationDifference("abc", "bac")
print("Output 1:", output1)

output2 = solution.findPermutationDifference("abcde", "edbac")
print("Output 2:", output2)
