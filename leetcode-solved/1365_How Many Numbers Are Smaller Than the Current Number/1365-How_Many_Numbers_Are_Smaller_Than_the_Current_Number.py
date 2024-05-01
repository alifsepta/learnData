class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        # Initialize a list to store the count of smaller numbers for each element
        result = []
        # Iterate through each element in nums
        for i in range(len(nums)):
            # Count the number of elements in nums that are smaller than nums[i]
            count = sum(1 for j in range(len(nums)) if nums[j] < nums[i])
            # Append the count to the result list
            result.append(count)
        return result

solution = Solution()
# Test cases
print(solution.smallerNumbersThanCurrent([8,1,2,2,3]))  # Output: [4,0,1,1,3]
print(solution.smallerNumbersThanCurrent([6,5,4,8]))    # Output: [2,1,0,3]
print(solution.smallerNumbersThanCurrent([7,7,7,7]))    # Output: [0,0,0,0]
