class Solution(object):
    def reversePrefix(self, word, ch):
        if ch not in word:  # Check if the character ch exists in the word
            return word  # If not, return the original word

        idx = word.index(ch)  # Find the index of the first occurrence of ch in the word
        return word[idx::-1] + word[idx + 1:]  # Return the reversed segment of word up to the index of ch inclusive, concatenated with the rest of the word

# Test cases
word1, ch1 = "abcdefd", "d"
word2, ch2 = "xyxzxe", "z"
word3, ch3 = "abcd", "z"

sol = Solution()
print(sol.reversePrefix(word1, ch1))  # Output: "dcbaefd"
print(sol.reversePrefix(word2, ch2))  # Output: "zxyxxe"
print(sol.reversePrefix(word3, ch3))  # Output: "abcd"
