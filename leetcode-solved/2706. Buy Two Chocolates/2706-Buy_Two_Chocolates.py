class Solution(object):
    def buyChoco(self, prices, money):
        # Sort the prices array in ascending order
        prices.sort()
        
        # If there are less than 2 prices, return the initial money
        if len(prices) < 2:
            return money
        
        # Calculate the sum of the two cheapest chocolates
        total_cost = prices[0] + prices[1]
        
        # If the initial money is more than or equal to the sum of the two cheapest chocolates
        if money >= total_cost:
            # Calculate the leftover money
            leftover = money - total_cost
            return leftover
        else:
            # If the initial money is not enough to buy the two cheapest chocolates, return the initial money
            return money

solution = Solution()

# Example 1
prices1 = [1, 2, 2]
money1 = 3
print(solution.buyChoco(prices1, money1))  # Output: 0

# Example 2
prices2 = [3, 2, 3]
money2 = 3
print(solution.buyChoco(prices2, money2))  # Output: 3
