# 832. Flipping an Image
[Problem Source](https://leetcode.com/problems/flipping-an-image/)

Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

- For example, flipping [1,1,0] horizontally results in [0,1,1]. To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

- For example, inverting [0,1,1] results in [1,0,0].


* Example 1:
    * Input: image = [[1,1,0],[1,0,1],[0,0,0]]
    * Output: [[1,0,0],[0,1,0],[1,1,1]]
    * Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]]. Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

* Example 2:
    * Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    * Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
    * Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

* Example 3:
    * Input: paths = [["A","Z"]]
    * Output: "Z"
    
* Constraints:
    - n == image.length
    - n == image[i].length
    - 1 <= n <= 20
    - images[i][j] is either 0 or 1.

## Process
1.  ```python
    class Solution(object):
    ```
    * This line defines a class named Solution.
    * It's a common convention to name this class Solution when solving LeetCode problems, but you can name it anything you like

2.  ```python
    def flipAndInvertImage(self, image):
    ```
    * This line defines a method named flipAndInvertImage inside the Solution class.
    * It takes two arguments: self (which refers to the instance of the class itself) and image.
    * image is expected to be a list of lists representing a binary image.

3.  ```python
    flipped_image = []
    ```
    * This line initializes an empty list named flipped_image to store the flipped and inverted image.
    
4.  ```python
    for row in image:
    ```
    * This line starts a loop that iterates over each row in the image.

5.  ```python
    flipped_row = [1 - pixel for pixel in reversed(row)]
    ```
    * This line reverses each row of the image (flips the image horizontally) and inverts it.
    * It uses a list comprehension to create a new list flipped_row, where each element pixel in the reversed row is subtracted from 1 to invert it.

6.  ```python
    flipped_image.append(flipped_row)
    ```
    * This line appends the flipped_row to the flipped_image list.

7.  ```python
    return flipped_image
    ```
    * This line returns the flipped_image, which contains the flipped and inverted image.

8.  ```python
    solution = Solution()
    ```
    * This line creates an instance of the Solution class.

9.  ```python
    print(solution.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
    ```
    * This line calls the flipAndInvertImage method of the solution object with the provided 3x3 binary image.
    * It prints the result, which should be the flipped and inverted image.

10.  ```python
    print(solution.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
    ```
    * This line calls the flipAndInvertImage method of the solution object with the provided 4x4 binary image.
    * It prints the result, which should be the flipped and inverted image
    


