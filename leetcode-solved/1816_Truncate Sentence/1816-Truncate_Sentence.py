class Solution(object):
    def truncateSentence(self, s, k):
        words = s.split()  # Splitting the sentence into words
        truncated_sentence = ' '.join(words[:k])  # Joining the first k words
        return truncated_sentence

solution = Solution()
print(solution.truncateSentence("Hello how are you Contestant", 4))  
print(solution.truncateSentence("What is the solution to this problem", 4)) 
print(solution.truncateSentence("chopper is not a tanuki", 5)) 
