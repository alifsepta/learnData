class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        merged_items = {}

        # Iterate through items1 and items2
        for item in items1 + items2:
            value, weight = item[0], item[1]
            # Update the merged_items dictionary with the total weight for each value
            if value in merged_items:
                merged_items[value] += weight
            else:
                merged_items[value] = weight

        # Convert the merged dictionary to a list of lists and sort it by value
        ret = sorted([[value, weight] for value, weight in merged_items.items()])

        return ret

# Example 1
solution = Solution()
items1_1 = [[1,1],[4,5],[3,8]]
items2_1 = [[3,1],[1,5]]
output_1 = solution.mergeSimilarItems(items1_1, items2_1)
print(output_1)  # Output: [[1, 6], [3, 9], [4, 5]]

# Example 2
items1_2 = [[1,1],[3,2],[2,3]]
items2_2 = [[2,1],[3,2],[1,3]]
output_2 = solution.mergeSimilarItems(items1_2, items2_2)
print(output_2)  # Output: [[1, 4], [2, 4], [3, 4]]

# Example 3
items1_3 = [[1,3],[2,2]]
items2_3 = [[7,1],[2,2],[1,4]]
output_3 = solution.mergeSimilarItems(items1_3, items2_3)
print(output_3)  # Output: [[1, 7], [2, 4], [7, 1]]
