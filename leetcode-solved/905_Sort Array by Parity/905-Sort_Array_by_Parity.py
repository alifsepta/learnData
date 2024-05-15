class Solution(object):
    def sortArrayByParity(self, nums):
        # Initialize two pointers, one at the beginning and one at the end of the array
        left, right = 0, len(nums) - 1
        
        # Loop until the two pointers meet or cross each other
        while left < right:
            # Check if the number at the left pointer is odd
            if nums[left] % 2 != 0:
                # If it's odd, swap it with the number at the right pointer if it's even
                if nums[right] % 2 == 0:
                    nums[left], nums[right] = nums[right], nums[left]
                # Move the right pointer to the left
                right -= 1
            else:
                # If the number at the left pointer is even, move the left pointer to the right
                left += 1
                
        # Return the modified array where even numbers are placed at the beginning
        return nums

# Create an instance of the Solution class
sol = Solution()

# Test case 1
nums1 = [3,1,2,4]
print(sol.sortArrayByParity(nums1))  # Output: [4, 2, 1, 3]

# Test case 2
nums2 = [0]
print(sol.sortArrayByParity(nums2))  # Output: [0]
