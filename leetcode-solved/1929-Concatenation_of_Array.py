#study case : https://leetcode.com/problems/concatenation-of-array/description/
class Solution(object):
    def getConcatenation(self, nums):
        n = len(nums)  # Get the length of the input list nums
        ans = [0] * (2 * n)  # Initialize ans with zeros of length 2 * n
        for i in range(n):
            ans[i] = nums[i]  # Assign nums[i] to ans[i]
            ans[i + n] = nums[i]  # Assign nums[i] to ans[i + n]
        return ans

# Test cases
solution = Solution()
print(solution.getConcatenation([1, 2, 1]))  
print(solution.getConcatenation([1, 3, 2, 1]))