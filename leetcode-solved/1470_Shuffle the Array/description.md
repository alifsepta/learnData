# 1470. Shuffle the Array
[Problem Source](https://leetcode.com/problems/shuffle-the-array/description/)

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

* Example 1:
    >Input: nums = [2,5,1,3,4,7], n = 3
    >Output: [2,3,5,4,1,7] 
    >Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
* Example 2:
    >Input: nums = [1,2,3,4,4,3,2,1], n = 4
    >Output: [1,4,2,3,3,2,4,1]
* Example 3:
    >Input: nums = [1,1,2,2], n = 2
    >Output: [1,2,1,2]
* Constraints:
    * 1 <= n <= 500
    * nums.length == 2n
    * 1 <= nums[i] <= 10^3 

## Process
1.  Define Class Name
    > This line defines a class named Solution. In Python, a class is a blueprint for creating objects. The (object) inside the parentheses indicates that Solution is inheriting from the base object class.
    ```python
    class Solution(object):
    ```
2.  Defines a method
    > This line defines a method called shuffle within the Solution class. Methods are functions defined inside a class. This method takes three parameters: self, which is a reference to the current instance of the class, nums, which is a list of integers, and n, which is an integer representing half the length of the nums list.
    ```python
    def shuffle(self, nums, n):
    ```
3.  Store the Suffleed Array
    > This line initializes an empty list called shuffled. This list will store the shuffled array that we'll create.
    ```python
    shuffled = [] 
    ```
4.  make a loop
    > This loop iterates n times, where n represents half the length of the nums list. Inside the loop, for each index i from 0 to n-1, it appends the element at index i from the nums list to shuffled, and then appends the element at index i + n from the nums list to shuffled. This effectively interleaves the x and y values from the nums list to form the shuffled array.
	```python
   	for i in range(n):
    shuffled.append(nums[i])
    shuffled.append(nums[i + n])
    ```
5.  return value
    > This line returns the shuffled list, which contains the desired shuffled array.
    ```python
    return shuffled

6. create instance
    > These lines create an instance of the Solution class called solution, then call the shuffle method with three different lists of integers and print the results. The shuffle method shuffles each input list according to the specified pattern and returns the shuffled lists.
    ```python
    solution = Solution()
    print(solution.shuffle([2,5,1,3,4,7], 3))
    print(solution.shuffle([1,2,3,4,4,3,2,1], 4))
    print(solution.shuffle([1,1,2,2], 2))
    ```
