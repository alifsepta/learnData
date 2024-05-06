class Solution(object):
    def sortSentence(self, s):
        # Split the input string s into a list of words based on space delimiter
        words = s.split()
        
        # Create a list to store the words in their original order
        original_order = [None] * len(words)
        
        # Iterate through each word in the shuffled sentence
        for word in words:
            # Extract the word itself by removing the last character (which is the index)
            word_text = word[:-1]
            # Extract the index from the last character of the word
            index = int(word[-1]) - 1  # Subtract 1 because index is 0-based
            # Assign the word to its original position in the list
            original_order[index] = word_text
        
        # Join the words in their original order to form the reconstructed sentence
        reconstructed_sentence = ' '.join(original_order)
        
        return reconstructed_sentence


s1 = "is2 sentence4 This1 a3"
solution = Solution()
print(solution.sortSentence(s1))

s2 = "Myself2 Me1 I4 and3"
print(solution.sortSentence(s2))
