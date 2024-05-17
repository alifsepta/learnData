class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()  # Sort the array in non-decreasing order

        # The maximum product difference will be the difference between the last and second-last elements
        # multiplied by the first and second elements, respectively.
        return nums[-1] * nums[-2] - nums[0] * nums[1]

# Example 1
nums1 = [5, 6, 2, 7, 4]
sol = Solution()
output1 = sol.maxProductDifference(nums1)
print("Output for nums1:", output1)

# Example 2
nums2 = [4, 2, 5, 9, 7, 4, 8]
output2 = sol.maxProductDifference(nums2)
print("Output for nums2:", output2)
