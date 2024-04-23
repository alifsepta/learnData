# 2549. Count Distinct Numbers on Board
[Problem Source](https://leetcode.com/problems/count-distinct-numbers-on-board/description/)

You are given a positive integer n, that is initially placed on a board. Every day, for 109 days, you perform the following procedure:

- For each number x present on the board, find all numbers 1 <= i <= n such that x % i == 1.
- Then, place those numbers on the board.

Return the number of distinct integers present on the board after 109 days have elapsed.

Note :

- Once a number is placed on the board, it will remain on it until the end.
- % stands for the modulo operation. For example, 14 % 3 is 2.


* Example 1:
    * Input: n = 5
    * Output: 4
    * Explanation: Initially, 5 is present on the board. The next day, 2 and 4 will be added since 5 % 2 == 1 and 5 % 4 == 1. After that day, 3 will be added to the board because 4 % 3 == 1. At the end of a billion days, the distinct numbers on the board will be 2, 3, 4, and 5.

* Example 2:
    * Input: n = 3
    * Output: 2
    * Explanation: Since 3 % 2 == 1, 2 will be added to the board. After a billion days, the only two distinct numbers on the board are 2 and 3. 
    
* Constraints:
    - 1 <= n <= 100

## Process
1.  ```python
    class Solution(object):
    ```
    * This line defines a class named Solution.

2.  ```python
    def distinctIntegers(self, n):
    ```
    * This line defines a method distinctIntegers inside the Solution class. This method takes one parameter n, which represents a positive integer.

3.  ```python
    if n == 1:
        return 1
    ```
    * This if statement checks if the input n is equal to 1. If it is, the method returns 1, as there will be only one distinct integer on the board.
    
4.  ```python
    return n - 1
    ```
    * If n is greater than 1, this line returns n - 1, as all numbers from 1 to n - 1 will be on the board.

5.  ```python
    print(solution.distinctIntegers(5))
    ```
    * This line calls the distinctIntegers method of the solution object with n = 5 and prints the result, which is 4.
    
6.  ```python
    print(solution.distinctIntegers(3))
    ```
    * This line calls the distinctIntegers method of the solution object with n = 3 and prints the result, which is 2.