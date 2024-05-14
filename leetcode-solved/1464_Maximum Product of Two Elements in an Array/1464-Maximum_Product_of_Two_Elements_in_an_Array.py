class Solution(object):
    def maxProduct(self, nums):
        # Sort the nums array in descending order
        nums.sort(reverse=True)
        
        # Calculate the maximum product by multiplying the two largest numbers in the sorted array
        max_product = (nums[0] - 1) * (nums[1] - 1)
        
        # Return the maximum product
        return max_product

# Example usage:
# Create an instance of the Solution class
solution = Solution()

# Test cases
nums1 = [3, 4, 5, 2]
nums2 = [1, 5, 4, 5]
nums3 = [3, 7]

# Call the maxProduct method on the instance with each test case
output1 = solution.maxProduct(nums1)
output2 = solution.maxProduct(nums2)
output3 = solution.maxProduct(nums3)

# Print the outputs
print(output1)  # Output: 12
print(output2)  # Output: 16
print(output3)  # Output: 12
