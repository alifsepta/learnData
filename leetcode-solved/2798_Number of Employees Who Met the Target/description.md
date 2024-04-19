# 2798. Number of Employees Who Met the Target
[Problem Source](https://leetcode.com/problems/number-of-employees-who-met-the-target/description/)

There are n employees in a company, numbered from 0 to n - 1. Each employee i has worked for hours[i] hours in the company.

The company requires each employee to work for at least target hours.

You are given a 0-indexed array of non-negative integers hours of length n and a non-negative integer target.

Return the integer denoting the number of employees who worked at least target hours.


* Example 1:
    * Input: hours = [0,1,2,3,4], target = 2
    * Output: 3
    * Explanation: The company wants each employee to work for at least 2 hours.
        - Employee 0 worked for 0 hours and didn't meet the target.
        - Employee 1 worked for 1 hours and didn't meet the target.
        - Employee 2 worked for 2 hours and met the target.
        - Employee 3 worked for 3 hours and met the target.
        - Employee 4 worked for 4 hours and met the target.
        - There are 3 employees who met the target.

* Example 2:
    * Input: hours = [5,1,4,2,2], target = 6
    * Output: 0
    * Explanation: The company wants each employee to work for at least 6 hours.
        - There are 0 employees who met the target.

* Constraints:
    - 1 <= n == hours.length <= 50
    - 0 <= hours[i], target <= 105

## Process
1.  Define Class Name
    > This line defines a class named Solution. In Python, a class is a blueprint for creating objects. The (object) inside the parentheses indicates that Solution is inheriting from the base object class.
    ```python
    class Solution(object):
    ```
2.  Defines a method
    > This line defines a method called numberOfEmployeesWhoMetTarget within the Solution class. Methods are functions defined inside a class. This method takes three parameters: self, which is a reference to the current instance of the class, hours, which is a list of integers representing the working hours of employees, and target, which is an integer representing the target number of hours.
    ```python
    def numberOfEmployeesWhoMetTarget(self, hours, target):
    ```
3.  Initialize variable
    > This line initializes a variable named count to 0. This variable will be used to count the number of employees who met the target number of hours.
    ```python
    count = 0
    ```
4.  make a loop
    > This line starts a loop that iterates through each element (hour) in the hours list.
	```python
    for hour in hours:
    ```
5.  Increment
    > If the condition is true (meaning the employee worked at least the target hours), this line increments the count variable by 1, indicating that one more employee met the target.
    ```python
    count += 1
    ```
6. return value
    > This line returns the final value of the count variable, which represents the number of employees who met the target number of hours.
    ```python
    return count
    ```
7. create instance
    > These lines create an instance of the Solution class called solution, then call the numberOfEmployeesWhoMetTarget method with two different lists of hours and target values, and print the results. The method calculates the number of employees who met the target hours for each input list.
    ```python
    solution = Solution()
    print(solution.numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2))
    print(solution.numberOfEmployeesWhoMetTarget([5,1,4,2,2], 6))
    ```