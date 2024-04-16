# 136. Single Number
[Problem Source](https://leetcode.com/problems/single-number/description/)

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

* Example 1:
    >Input: nums = [2,2,1]
    >Output: 1
* Example 2:
    >Input: nums = [4,1,2,1,2]
    >Output: 4
* Example 3:
    >Input: nums = [1]
    >Output: 1
* Constraints:
    * 1 <= nums.length <= 3 * 104
    * -3 * 104 <= nums[i] <= 3 * 104
    * Each element in the array appears twice except for one element which appears only once.

## Process
1.  Define Class Name
    > This line defines a class named Solution. In Python, a class is a blueprint for creating objects. The (object) inside the parentheses indicates that Solution is inheriting from the base object class.
    ```python
    class Solution(object):
    ```
2.  Defines a method
    > This line defines a method called singleNumber within the Solution class. Methods are functions defined inside a class. This method takes two parameters: self, which is a reference to the current instance of the class, and nums, which is a list of integers.
    ```python
    def singleNumber(self, nums):
    ```
3.  Initiate variable
    >This line initializes a variable result to 0. This variable will be used to store the result of the operation.
    ```python
    result = 0
    ```
4.  make a loop
    > This line starts a loop that iterates through each element (num) in the nums list. The loop variable num will take on each value in the list, one at a time.
    ```python
    for num in nums:
    ```
5.  Cancel twice number using property XOR
    > This line uses the bitwise XOR (^) operation to update the result variable. The XOR operation has the property that if you XOR a number with itself, the result is 0. So, by XORing all the numbers in the list, each number that appears twice will cancel each other out, leaving only the single number.
    ```python
    result ^= num
    ```
6.  returns value
    > This line returns the value stored in the result variable, which represents the single number that appears only once in the nums list.
    ```python
    return result
    ```
7.  create instance
    > These lines create an instance of the Solution class called solution, then call the singleNumber method with three different lists of integers and print the results. The singleNumber method calculates the single number that appears only once in each list and returns it.
    ```python
    solution = Solution()
    print(solution.singleNumber([2,2,1]))
    print(solution.singleNumber([4,1,2,1,2]))   
    print(solution.singleNumber([1]))
    ```

