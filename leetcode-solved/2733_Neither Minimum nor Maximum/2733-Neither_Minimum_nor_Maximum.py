def findMiddleElement(nums):
    # Sorting the array in ascending order
    nums.sort()
    
    # If the length of the array is less than 3, there is no valid middle element
    if len(nums) < 3:
        return -1
    
    # The middle element is at index 1 from the sorted array, as the first element would be the minimum
    # and the last element would be the maximum
    return nums[1]

# Example 1
nums1 = [3, 2, 1, 4]
print("Example 1 Output:", findMiddleElement(nums1))

# Example 2
nums2 = [1, 2]
print("Example 2 Output:", findMiddleElement(nums2))

# Example 3
nums3 = [2, 1, 3]
print("Example 3 Output:", findMiddleElement(nums3))
