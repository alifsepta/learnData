class Solution(object):
    def finalString(self, s):
        # Initialize an empty string to store the final result
        result = ""
        
        # Iterate over each character in the input string
        for char in s:
            # If the character is not 'i', simply append it to the result string
            if char != 'i':
                result += char
            else:
                # If the character is 'i', reverse the current result string
                result = result[::-1]
        
        # Return the final result after traversing the entire input string
        return result

# Test cases
solution = Solution()
print(solution.finalString("string"))  # Output: "rtsng"
print(solution.finalString("poiinter"))  # Output: "ponter"
