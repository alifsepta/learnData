class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        flipped_image = []  # Initialize an empty list to store the flipped image
        
        # Iterate through each row in the image
        for row in image:
            # Reverse the row (flip the image horizontally) and invert it
            flipped_row = [1 - pixel for pixel in reversed(row)]
            flipped_image.append(flipped_row)  # Add the flipped and inverted row to the flipped_image list
        
        return flipped_image

# Test cases
solution = Solution()
print(solution.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))  # Output: [[1,0,0],[0,1,0],[1,1,1]]
print(solution.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))  # Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
