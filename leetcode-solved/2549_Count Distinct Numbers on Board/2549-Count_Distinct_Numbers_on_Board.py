class Solution(object):
    def distinctIntegers(self, n):
        if n == 1:
            return 1  # If n is 1, there will be only one distinct integer
        
        return n - 1  # For all n > 1, all integers from 1 to n - 1 will be present

solution = Solution()
print(solution.distinctIntegers(5))  # Output: 4
print(solution.distinctIntegers(3))  # Output: 2
