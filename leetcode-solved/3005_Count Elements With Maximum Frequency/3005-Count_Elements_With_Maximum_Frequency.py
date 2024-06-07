class Solution(object):
    def maxFrequencyElements(self, nums):
        # Count the frequency of each element using a dictionary
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # Find the maximum frequency
        max_freq = max(freq_map.values())
        
        # Count the total occurrences of elements with maximum frequency
        total_occurrences = sum(freq for freq in freq_map.values() if freq == max_freq)
        
        return total_occurrences

# Instantiate the Solution class
sol = Solution()

# Example 1 input
nums1 = [1, 2, 2, 3, 1, 4]
# Example 1 output
print("Example 1 output:", sol.maxFrequencyElements(nums1))

# Example 2 input
nums2 = [1, 2, 3, 4, 5]
# Example 2 output
print("Example 2 output:", sol.maxFrequencyElements(nums2))
