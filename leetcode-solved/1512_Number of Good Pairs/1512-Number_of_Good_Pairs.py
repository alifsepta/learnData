class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize a dictionary to count occurrences of each number
        num_counts = {}
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1
        
        # Initialize a variable to store the total number of good pairs
        good_pairs = 0
        
        # Iterate through the dictionary
        for count in num_counts.values():
            # Calculate the number of good pairs for each number
            good_pairs += count * (count - 1) // 2
        
        return good_pairs

# Test cases
solution = Solution()
print(solution.numIdenticalPairs([1,2,3,1,1,3]))   # Output: 4
print(solution.numIdenticalPairs([1,1,1,1]))       # Output: 6
print(solution.numIdenticalPairs([1,2,3]))         # Output: 0
