class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize result variable
        result = 0
        
        # Iterate through each number in nums
        for num in nums:
            # XOR the result with the current number
            result ^= num
        
        # The result will be the single number
        return result

# Test cases
solution = Solution()
print(solution.singleNumber([2,2,1]))   # Output: 1
print(solution.singleNumber([4,1,2,1,2]))   # Output: 4
print(solution.singleNumber([1]))   # Output: 1
