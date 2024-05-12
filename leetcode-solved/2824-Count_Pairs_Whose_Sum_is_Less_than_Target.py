class Solution(object):
    def countPairs(self, nums, target):
        # Initialize a variable to keep track of the count of pairs
        count = 0
        # Iterate through each index i
        for i in range(len(nums)):
            # Iterate through each index j starting from i+1
            for j in range(i+1, len(nums)):
                # Check if the sum of nums[i] and nums[j] is less than the target
                if nums[i] + nums[j] < target:
                    # If yes, increment the count of pairs
                    count += 1
        # Finally, return the count of pairs
        return count

# Create an instance of the Solution class
sol = Solution()

# Test cases
nums1 = [-1, 1, 2, 3, 1]
target1 = 2
output1 = sol.countPairs(nums1, target1)
print("Output 1:", output1)  # Expected output: 3

nums2 = [-6, 2, 5, -2, -7, -1, 3]
target2 = -2
output2 = sol.countPairs(nums2, target2)
print("Output 2:", output2)  # Expected output: 10
