class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        # Sort the boxTypes based on the number of units per box in descending order
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        total_units = 0
        
        for boxes, units_per_box in boxTypes:
            # If the truck has enough space for all boxes of this type
            if truckSize >= boxes:
                total_units += boxes * units_per_box
                truckSize -= boxes
            # If the truck has limited space, take as many boxes as possible
            else
                total_units += truckSize * units_per_box
                break  # No need to check other box types, as the truck is full
        
        return total_units

# Example 1
boxTypes1 = [[1,3],[2,2],[3,1]]
truckSize1 = 4
sol = Solution()
print(sol.maximumUnits(boxTypes1, truckSize1))  # Output: 8

# Example 2
boxTypes2 = [[5,10],[2,5],[4,7],[3,9]]
truckSize2 = 10
print(sol.maximumUnits(boxTypes2, truckSize2))  # Output: 91
