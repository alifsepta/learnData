# 121. Best Time to Buy and Sell Stock
[Problem Source](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

* Example 1:

    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell

* Example 2:

    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.

* Constraints:

    1 <= prices.length <= 105
    0 <= prices[i] <= 104

## Process
1.  Define Class Name
    > This class will contain the method to solve the problem of maximizing profit from buying and selling stocks.
    ```python
    class Solution(object):
    ```
2.  Defines a method
    > This method takes two parameters: self, which refers to the instance of the class, and prices, which is a list representing the prices of the stock on each day.
    ```python
    def maxProfit(self, prices):
    ```
3.  if condition
    >This line checks if the prices list is empty. If it is empty, it means there are no prices to analyze, so the method returns 0 as the maximum profit.
    ```python
            if not prices:
            return 0
    ```
4.  initializes variable
    > This line initializes a variable max_profit to 0. This variable will keep track of the maximum profit that can be achieved.
    ```python
    max_profit = 0
    ```
5.  initialize variable_2
    > This line initializes a variable min_price to the first price in the prices list. This variable will keep track of the minimum price seen so far.
    ```python
    min_price = prices[0]
    ```
6.  make a loop
    > This line starts a loop that iterates through each price in the prices list. The loop variable price will take on each value in the list, one at a time.
    ```python
    for price in prices:
    ```
7.  ensure condition of variable
    > This line updates the min_price variable to be the minimum of the current min_price and the current price. This ensures that min_price always holds the lowest price seen so far.
    ```python
    min_price = min(min_price, price)
    ```
8.  ensure condition of variable_2
    > This line updates the max_profit variable to be the maximum of the current max_profit and the difference between the current price and the min_price. This calculates the potential profit if the stock is sold at the current price after being bought at min_price.
    ```python
    max_profit = max(max_profit, price - min_price)
    ```
9. return variable
    > This line returns the max_profit variable, which represents the maximum profit that can be achieved from buying and selling the stock according to the given prices.
    > The rest of the code consists of creating an instance of the Solution class and calling the maxProfit method with example test cases to demonstrate its functionality.
    ```python
    return max_profit
    ```
