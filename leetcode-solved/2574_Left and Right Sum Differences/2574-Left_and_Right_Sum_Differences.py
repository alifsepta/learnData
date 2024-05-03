class Solution(object):
    def leftRightDifference(self, nums):
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n

        curr_left_sum = 0
        for i in range(n):
            curr_left_sum += nums[i]
            leftSum[i] = curr_left_sum

        curr_right_sum = 0
        for i in range(n - 1, -1, -1):
            curr_right_sum += nums[i]
            rightSum[i] = curr_right_sum

        answer = [abs(leftSum[i] - rightSum[i]) for i in range(n)]

        return answer
