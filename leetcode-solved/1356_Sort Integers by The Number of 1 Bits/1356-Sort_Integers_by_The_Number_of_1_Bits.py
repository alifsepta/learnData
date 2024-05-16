class Solution(object):
    def sortByBits(self, arr):
        # Define a custom sorting function to sort based on the number of set bits (1s) in the binary representation
        def count_bits(num):
            return bin(num).count('1')
        
        # Sort the array 'arr' using the custom sorting function count_bits and then by the number itself
        arr.sort(key=lambda x: (count_bits(x), x))
        
        # Return the sorted array
        return arr

# Create an instance of the Solution class
sol = Solution()

# Example 1 input
arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# Example 2 input
arr2 = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

# Print the output of sorting for both examples
print(sol.sortByBits(arr1))
print(sol.sortByBits(arr2))
