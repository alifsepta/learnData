class Solution(object):
    def buildArray(self, nums):
        # Initialize an empty list to store the result
        ans = []
        
        # Iterate through each index i in the range of the length of nums
        for i in range(len(nums)):
            # Append nums[nums[i]] to the result list
            ans.append(nums[nums[i]])
        
        # Return the resulting list
        return ans

# Create an instance of the Solution class
solution = Solution()

# Test cases
nums_1 = [0,2,1,5,3,4]
nums_2 = [5,0,1,2,3,4]

# Print the outputs for each test case
print(solution.buildArray(nums_1))  # Output: [0,1,2,4,5,3]
print(solution.buildArray(nums_2))  # Output: [4,5,0,1,2,3]
