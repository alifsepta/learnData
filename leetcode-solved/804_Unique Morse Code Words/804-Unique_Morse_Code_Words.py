class Solution(object):
    def uniqueMorseRepresentations(self, words):
        # Define the Morse code representation for each letter
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        # Create a set to store unique transformations
        transformations = set()

        # Iterate through each word in the input list
        for word in words:
            # Initialize an empty string to store the transformation of the current word
            morse_word = ""
            # Iterate through each character in the current word
            for char in word:
                # Find the index of the character in the alphabet (a=0, b=1, ..., z=25)
                index = ord(char) - ord('a')
                # Append the Morse code representation of the character to the morse_word string
                morse_word += morse_code[index]
            
            # Add the transformed word to the set of transformations
            transformations.add(morse_word)

        # Return the number of unique transformations
        return len(transformations)

# Test the solution
solution = Solution()
words1 = ["gin","zen","gig","msg"]
print(solution.uniqueMorseRepresentations(words1))  # Output: 2
words2 = ["a"]
print(solution.uniqueMorseRepresentations(words2))  # Output: 1
