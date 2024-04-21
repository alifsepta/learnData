# 1436. Destination City
[Problem Source](https://leetcode.com/problems/destination-city/)

You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.


* Example 1:
    * Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    * Output: "Sao Paulo" 
    * Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

* Example 2:
    * Input: paths = [["B","C"],["D","B"],["C","A"]]
    * Output: "A"
    * Explanation: All possible trips are: 
        - "D" -> "B" -> "C" -> "A". 
        - "B" -> "C" -> "A".  
        - "C" -> "A". 
        - "A". 
        - Clearly the destination city is "A".

* Example 3:
    * Input: paths = [["A","Z"]]
    * Output: "Z"
    
* Constraints:
    - 1 <= paths.length <= 100
    - paths[i].length == 2
    - 1 <= cityAi.length, cityBi.length <= 10
    - cityAi != cityBi
    - All strings consist of lowercase and uppercase English letters and the space character.

## Process
1.  Define Class Name
    > Defines a class named Solution.
    ```python
    class Solution(object):
    ```
2.  Defines a method
    > Defines a method destCity inside the Solution class. This method takes a list of lists paths as input, where each inner list represents a path from one city to another. The method returns a string, which is the destination city.
    ```python
     def destCity(self, paths):
    ```
3.  make a loop
    > Iterates through each path in the paths list. For each path, it adds the starting city (path[0]) to the starts set and the destination city (path[1]) to the destinations set.
    ```python
    for path in paths:
        starts.add(path[0])  
        destinations.add(path[1])  
    ```
4.  make a loop
    > Iterates through the destinations set. Checks if each city is not in the starts set. If a city is found that is not a starting city, it means it's the destination city, so it returns that city.
	```python
    for city in destinations:
        if city not in starts:
        return city
    ```

5. create instance
    > Creates an instance of the Solution class named solution. Calls the destCity method with three different lists of paths and prints the results. The method returns the destination city for each list of paths.
    ```python
    solution = Solution()
    print(solution.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))  #   Output: "Sao Paulo"
    print(solution.destCity([["B","C"],["D","B"],["C","A"]]))  
    print(solution.destCity([["A","Z"]]))  
    ```
