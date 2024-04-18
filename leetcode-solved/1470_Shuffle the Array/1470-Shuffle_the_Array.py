class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        shuffled = []  # Initialize an empty list to store the shuffled array
        
        # Iterate over the range from 0 to n (exclusive)
        for i in range(n):
            # Append the ith element of x values (nums[i]) to shuffled
            shuffled.append(nums[i])
            # Append the ith element of y values (nums[i + n]) to shuffled
            shuffled.append(nums[i + n])
        
        return shuffled

# Test cases
solution = Solution()
print(solution.shuffle([2,5,1,3,4,7], 3))   # Output: [2,3,5,4,1,7]
print(solution.shuffle([1,2,3,4,4,3,2,1], 4))   # Output: [1,4,2,3,3,2,4,1]
print(solution.shuffle([1,1,2,2], 2))   # Output: [1,2,1,2]
