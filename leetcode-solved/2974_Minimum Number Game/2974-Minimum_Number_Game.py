class Solution(object):
    def numberGame(self, nums):
        # Initialize an empty array to store the resulting arrangement
        arr = []
        
        # Sort the nums array in ascending order
        nums.sort()
        
        # Iterate until nums array becomes empty
        while nums:
            # Alice removes the minimum element from nums
            alice_move = nums.pop(0)
            # Bob removes the minimum element from nums
            bob_move = nums.pop(0)
            
            # Bob appends the removed element to arr
            arr.append(bob_move)
            # Alice appends her removed element to arr
            arr.append(alice_move)
        
        # Return the resulting array arr
        return arr

# Create an instance of the Solution class
sol = Solution()

# Example 1
nums1 = [5, 4, 2, 3]
output1 = sol.numberGame(nums1)
print(output1)  # Output: [3, 2, 5, 4]

# Example 2
nums2 = [2, 5]
output2 = sol.numberGame(nums2)
print(output2)  # Output: [5, 2]
