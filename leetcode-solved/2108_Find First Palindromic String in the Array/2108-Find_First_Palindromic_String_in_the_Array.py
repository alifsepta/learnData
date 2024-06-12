class Solution(object):
    def firstPalindrome(self, words):
        # Define a function to check if a string is a palindrome
        def isPalindrome(s):
            return s == s[::-1]
        
        # Iterate through each word in the list of words
        for word in words:
            # Check if the current word is a palindrome using the isPalindrome function
            if isPalindrome(word):
                # If it is, return the word
                return word
        # If no palindrome is found, return an empty string
        return ""

# Example cases
words1 = ["abc","car","ada","racecar","cool"]
words2 = ["notapalindrome","racecar"]
words3 = ["def","ghi"]

# Create an instance of the Solution class
sol = Solution()

# Test the examples
print(sol.firstPalindrome(words1))  # Output: "ada"
print(sol.firstPalindrome(words2))  # Output: "racecar"
print(sol.firstPalindrome(words3))  # Output: ""
