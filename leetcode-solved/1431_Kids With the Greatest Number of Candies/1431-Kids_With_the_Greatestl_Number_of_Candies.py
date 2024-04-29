class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        # Find the maximum number of candies among all kids
        max_candies = max(candies)
        
        # Create a list to store the result whether each kid can have the greatest number of candies
        result = []
        
        # Iterate through each kid's candies
        for candy in candies:
            # Check if the current kid, after receiving extraCandies, will have the greatest number of candies
            # and append the result to the result list
            result.append(candy + extraCandies >= max_candies)
        
        # Return the result list
        return result

solution = Solution()
print(solution.kidsWithCandies([2,3,5,1,3], 3))
print(solution.kidsWithCandies([4,2,1,1,2], 1))
print(solution.kidsWithCandies([12,1,12], 10))
