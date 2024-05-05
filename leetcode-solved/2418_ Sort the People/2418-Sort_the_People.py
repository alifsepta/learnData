class Solution(object):
    def sortPeople(self, names, heights):
        # Combine names and heights into a list of tuples where each tuple contains a name and its corresponding height
        # This allows us to sort them together while preserving the association between names and heights
        people = [(names[i], heights[i]) for i in range(len(names))]
        
        # Sort the list of tuples in descending order based on the height (second element of each tuple)
        people.sort(key=lambda x: x[1], reverse=True)
        
        # Extract the names from the sorted list of tuples
        sorted_names = [person[0] for person in people]
        
        # Return the sorted names
        return sorted_names

# Example 1
names1 = ["Mary", "John", "Emma"]
heights1 = [180, 165, 170]
solution1 = Solution()
print(solution1.sortPeople(names1, heights1))  # Output: ["Mary", "Emma", "John"]

# Example 2
names2 = ["Alice", "Bob", "Bob"]
heights2 = [155, 185, 150]
solution2 = Solution()
print(solution2.sortPeople(names2, heights2))  # Output: ["Bob", "Alice", "Bob"]