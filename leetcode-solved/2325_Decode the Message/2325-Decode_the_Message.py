class Solution(object):
    def decodeMessage(self, key, message):
        # Step 1: Create a substitution table based on the key
        substitution_table = self.create_substitution_table(key)
        
        # Step 2: Decode the message using the substitution table
        decoded_message = self.decode_with_substitution_table(message, substitution_table)
        
        return decoded_message
    
    def create_substitution_table(self, key):
        # Initialize an empty substitution table
        substitution_table = {}
        
        # Initialize index for mapping letters to positions
        index = 0
        
        # Iterate through each character in the key
        for char in key:
            # If the character is not a space and it's not already in the table
            if char != ' ' and char not in substitution_table:
                # Map the character to the corresponding position in the alphabet
                substitution_table[char] = chr(ord('a') + index)
                index += 1
                
        return substitution_table
    
    def decode_with_substitution_table(self, message, substitution_table):
        # Initialize an empty decoded message
        decoded_message = ''
        
        # Iterate through each character in the message
        for char in message:
            # If the character is a space, add it directly to the decoded message
            if char == ' ':
                decoded_message += ' '
            # If the character is in the substitution table, replace it with the corresponding letter
            elif char in substitution_table:
                decoded_message += substitution_table[char]
        
        return decoded_message

# Create an instance of the Solution class
sol = Solution()

# Example 1
key1 = "the quick brown fox jumps over the lazy dog"
message1 = "vkbs bs t suepuv"
output1 = sol.decodeMessage(key1, message1)
print(output1)  # Output should be "this is a secret"

# Example 2
key2 = "eljuxhpwnyrdgtqkviszcfmabo"
message2 = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
output2 = sol.decodeMessage(key2, message2)
print(output2)  # Output should be "the five boxing wizards jump quickly"
