# 1672. Richest Customer Wealth
[Problem Source](https://leetcode.com/problems/richest-customer-wealth/description/)

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

Return the integer denoting the number of employees who worked at least target hours.


* Example 1:
    * Input: accounts = [[1,2,3],[3,2,1]]
    * Output: 6
    * Explanation:
        - 1st customer has wealth = 1 + 2 + 3 = 6
        - 2nd customer has wealth = 3 + 2 + 1 = 6
        - Both customers are considered the richest with a wealth of 6 each, so return 6.

* Example 2:
    * Input: accounts = [[1,5],[7,3],[3,5]]
    * Output: 10
    * Explanation: 
        - 1st customer has wealth = 6
        - 2nd customer has wealth = 10 
        - 3rd customer has wealth = 8
        - The 2nd customer is the richest with a wealth of 10.

* Example 3:
    * Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
    * Output: 17
    
* Constraints:
    - m == accounts.length
    - n == accounts[i].length
    - 1 <= m, n <= 50
    - 1 <= accounts[i][j] <= 100

## Process
1.  Define Class Name
    > This line defines a class named Solution. In Python, a class is a blueprint for creating objects. The (object) inside the parentheses indicates that Solution is inheriting from the base object class.
    ```python
    class Solution(object):
    ```
2.  Defines a method
    > This line defines a method named maximumWealth within the Solution class. Methods are functions defined inside a class. This method takes two parameters: self, which is a reference to the current instance of the class, and accounts, which is a list of lists of integers representing the amount of money each customer has in their bank accounts. The method returns an integer, which is the maximum wealth among all customers.
    ```python
    def maximumWealth(self, accounts):
    ```
3.  Initialize variable
    > This line initializes a variable named max_wealth to 0. This variable will be used to store the maximum wealth found among all customers.
    ```python
    max_wealth = 0
    ```
4.  make a loop
    > This line starts a loop that iterates through each customer in the accounts list.
	```python
    for customer in accounts:
    ```
5.  calculates wealth
    > For each customer, this line calculates their wealth by summing up the amounts in their bank accounts using the sum() function.
    ```python
    wealth = sum(customer)
    ```
6. find maximum wealth
    > This line updates the max_wealth variable with the maximum of the current customer's wealth (wealth) and the maximum wealth found so far (max_wealth) using the max() function.
    ```python
    max_wealth = max(max_wealth, wealth)
    ```
7. return value
    > This line returns the final value of the max_wealth variable, which represents the maximum wealth among all customers.
    ```python
    return max_wealth
    ```

8. create instance
    > These lines create an instance of the Solution class called solution, then call the maximumWealth method with three different lists of accounts and print the results. The method calculates the maximum wealth among all customers for each input list.
    ```python
    solution = Solution()
    print(solution.maximumWealth([[1,2,3],[3,2,1]]))
    print(solution.maximumWealth([[1,5],[7,3],[3,5]]))
    print(solution.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))
    ```
