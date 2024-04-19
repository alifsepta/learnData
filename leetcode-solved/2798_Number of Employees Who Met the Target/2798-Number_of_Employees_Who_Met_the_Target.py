class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        count = 0  # Initialize a variable to count the number of employees who met the target
        
        # Iterate through each element in the hours array
        for hour in hours:
            # Check if the current employee worked at least the target number of hours
            if hour >= target:
                # If so, increment the count of employees who met the target
                count += 1
        
        return count

# Test cases
solution = Solution()
print(solution.numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2))  # Output: 3
print(solution.numberOfEmployeesWhoMetTarget([5,1,4,2,2], 6))  # Output: 0
