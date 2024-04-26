class Solution(object):
    def mostWordsFound(self, sentences):
        max_words = 0  # Initialize the maximum number of words
        for sentence in sentences:  # Iterate through each sentence
            words = sentence.split()  # Split the sentence into words
            max_words = max(max_words, len(words))  # Update max_words if the current sentence has more words
        return max_words  # Return the maximum number of words found in a single sentence
    
solution = Solution()
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(solution.mostWordsFound(sentences))  
sentences = ["please wait", "continue to fight", "continue to win"]
print(solution.mostWordsFound(sentences))
