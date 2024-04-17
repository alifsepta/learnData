# 1512. Number of Good Pairs
[Problem Source](https://leetcode.com/problems/number-of-good-pairs/)

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

* Example 1:
    >Input: nums = [1,2,3,1,1,3]
    >Output: 4
    >Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
* Example 2:
    >Input: nums = [1,1,1,1]
    >Output: 6
    >Explanation: Each pair in the array are good.
* Example 3:
    >Input: nums = [1,2,3]
    >Output: 0
* Constraints:
    * 1 <= nums.length <= 100
    * 1 <= nums[i] <= 100

## Process
1.  Define Class Name
    > This line defines a class named Solution. In Python, a class is a blueprint for creating objects. The (object) inside the parentheses indicates that Solution is inheriting from the base object class.
    ```python
    class Solution(object):
    ```
2.  Defines a method
    > This line defines a method called numIdenticalPairs within the Solution class. Methods are functions defined inside a class. This method takes two parameters: self, which is a reference to the current instance of the class, and nums, which is a list of integers.
    ```python
    def numIdenticalPairs(self, nums):
    ```
3.  Initiate variable
    >This line initializes an empty dictionary called num_counts. This dictionary will be used to count the occurrences of each number in the nums list.
    ```python
	num_counts = {}
    ```
4.  make a loop
    > These lines iterate through each number in the nums list. For each number, it checks if the number already exists as a key in the num_counts dictionary. If it does, it increments its count by 1. If not, it initializes its count to 1 using the .get() method.
	```python
   	for num in nums:
	num_counts[num] = num_counts.get(num, 0) + 1
    ```
5.  Initializes variable
    > This line initializes a variable called good_pairs to 0. This variable will be used to count the total number of good pairs.
    ```python
    good_pairs = 0
    ```
6.  iterate
    > These lines iterate through the values of the num_counts dictionary, which represent the counts of each number. For each count, it calculates the number of good pairs using the formula (count * (count - 1)) // 2 and adds it to the good_pairs variable.
    ```python
    for count in num_counts.values():
    good_pairs += count * (count - 1) //2
    ```
7.  return value
    > This line returns the total number of good pairs calculated in the previous step.
    ```python
    return good_pairs
    ```

8. create instance
    > These lines create an instance of the Solution class called solution, then call the numIdenticalPairs method with three different lists of integers and print the results. The numIdenticalPairs method calculates the number of good pairs in each list and returns it.
    ```python
    solution = Solution()
    print(solution.numIdenticalPairs([1,2,3,1,1,3]))
    print(solution.numIdenticalPairs([1,1,1,1]))
    print(solution.numIdenticalPairs([1,2,3]))
    ```
