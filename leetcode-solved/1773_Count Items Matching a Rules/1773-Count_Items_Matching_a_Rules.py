class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        rule_index = {"type": 0, "color": 1, "name": 2}
        count = 0
        for item in items:
            if item[rule_index[ruleKey]] == ruleValue:
                count += 1
        return count

solution = Solution()
print(solution.countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver")) # Output: 1
print(solution.countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", "phone")) # Output: 2
