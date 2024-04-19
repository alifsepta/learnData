# 2942. Find Words Containing Character
[Problem Source](https://leetcode.com/problems/find-words-containing-character/description/)

You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note: that the returned array may be in any order.

* Example 1:
    > Input: words = ["leet","code"], x = "e"
    > Output: [0,1]
    > Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.
* Example 2:
    > Input: words = ["abc","bcd","aaaa","cbc"], x = "a"
    > Output: [0,2]
    > Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and 2.
* Example 3:
    > Input: words = ["abc","bcd","aaaa","cbc"], x = "z"
    > Output: []
    > Explanation: "z" does not occur in any of the words. Hence, we return an empty array.
* Constraints:
    * 1 <= words.length <= 50
    * 1 <= words[i].length <= 50
    * x is a lowercase English letter.
    * words[i] consists only of lowercase English letters.

## Process
1.  Define Class Name
    > This line defines a class named Solution. In Python, a class is a blueprint for creating objects. The (object) inside the parentheses indicates that Solution is inheriting from the base object class.
    ```python
    class Solution(object):
    ```
2.  Defines a method
    > This line defines a method called findWordsContaining within the Solution class. Methods are functions defined inside a class. This method takes three parameters: self, which is a reference to the current instance of the class, words, which is a list of strings, and x, which is a string representing the character to search for.
    ```python
    def findWordsContaining(self, words, x):
    ```
3.  Initialize empty list
    > This line initializes an empty list called indices. This list will store the indices of words that contain the character x.
    ```python
    indices = []
    ```
4.  make a loop
    > This line starts a loop that iterates through each word in the words list. The enumerate function is used to iterate through both the indices (i) and the words (word) in the list.
	```python
    for i, word in enumerate(words):
    ```
5.  check character
    > This line checks if the character x is present in the current word using the in operator.
    ```python
    if x in word:
    ```
6. appends
    > If the character x is found in the current word, this line appends the index (i) of the current word to the indices list.
    ```python
    indices.append(i)
    ```
7. returns value
    > This line returns the indices list, which contains the indices of words that contain the character x.
    ```python
    return indices
    ```
8. creat instance
    > These lines create an instance of the Solution class called solution, then call the findWordsContaining method with three different lists of words and a character x, and print the results. The findWordsContaining method returns the indices of words containing the character x in each list.
    ```python
    solution = Solution()
    print(solution.findWordsContaining(["leet","code"], "e"))
    print(solution.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "a"))
    print(solution.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "z"))
    ```