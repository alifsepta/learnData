class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0  # Initialize a variable to store the maximum wealth found
        
        # Iterate through each customer's accounts
        for customer in accounts:
            # Calculate the wealth of the current customer by summing up their account amounts
            wealth = sum(customer)
            # Update the maximum wealth if the current customer's wealth is greater
            max_wealth = max(max_wealth, wealth)
        
        return max_wealth

# Test cases
solution = Solution()
print(solution.maximumWealth([[1,2,3],[3,2,1]]))  # Output: 6
print(solution.maximumWealth([[1,5],[7,3],[3,5]]))  # Output: 10
print(solution.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))  # Output: 17
