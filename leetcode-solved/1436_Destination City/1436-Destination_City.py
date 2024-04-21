class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        destinations = set()  # Initialize a set to store all destination cities
        starts = set()  # Initialize a set to store all starting cities
        
        # Iterate through each path
        for path in paths:
            starts.add(path[0])  # Add the starting city to the starts set
            destinations.add(path[1])  # Add the destination city to the destinations set
        
        # The destination city is the city that is in the destinations set but not in the starts set
        for city in destinations:
            if city not in starts:
                return city

# Test cases
solution = Solution()
print(solution.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))  # Output: "Sao Paulo"
print(solution.destCity([["B","C"],["D","B"],["C","A"]]))  # Output: "A"
print(solution.destCity([["A","Z"]]))  # Output: "Z"
