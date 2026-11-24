class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        i = 0
        j = k - 1
        oldSum = sum(nums[:k])
        maxSum = oldSum
        while j < len(nums)-1:
            newSum = oldSum - nums[i] + nums[j+1]
            maxSum = max(maxSum, newSum)
            oldSum = newSum
            j += 1
            i += 1
        return maxSum / k