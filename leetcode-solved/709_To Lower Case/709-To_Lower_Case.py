class Solution(object):
    def toLowerCase(self, s):
        # Initialize an empty string to store the result
        result = ""
        
        # Iterate through each character in the input string
        for char in s:
            # Check if the character is an uppercase letter
            if 'A' <= char <= 'Z':
                # If yes, convert it to lowercase using ASCII manipulation
                # ASCII value difference between uppercase and lowercase letters is 32
                # So, we add 32 to the ASCII value of the uppercase letter to convert it to lowercase
                result += chr(ord(char) + 32)
            else:
                # If the character is not an uppercase letter, simply append it to the result string
                result += char
        
        # Return the final result string
        return result

# Test cases
solution = Solution()
print(solution.toLowerCase("Hello"))  # Output: "hello"
print(solution.toLowerCase("here"))   # Output: "here"
print(solution.toLowerCase("LOVELY")) # Output: "lovely"
