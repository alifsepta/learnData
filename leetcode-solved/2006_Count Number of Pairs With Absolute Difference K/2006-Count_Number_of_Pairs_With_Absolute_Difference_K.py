class Solution(object):
    def countKDifference(self, nums, k):
        # Initialize a variable to store the count of pairs
        count = 0
        
        # Loop through all possible pairs of indices (i, j) in nums
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Check if the absolute difference between nums[i] and nums[j] equals k
                if abs(nums[i] - nums[j]) == k:
                    # If so, increment the count
                    count += 1
        
        # Return the total count of pairs with an absolute difference of k
        return count

# Create an instance of the Solution class
sol = Solution()

# Test Example 1
nums1 = [1, 2, 2, 1]
k1 = 1
print(sol.countKDifference(nums1, k1))  # Output should be 4

# Test Example 2
nums2 = [1, 3]
k2 = 3
print(sol.countKDifference(nums2, k2))  # Output should be 0

# Test Example 3
nums3 = [3, 2, 1, 5, 4]
k3 = 2
print(sol.countKDifference(nums3, k3))  # Output should be 3
