class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        expectedSum=sum(range(0,len(nums)+1))     #greater value
        newNums=set(nums)
        actualSum=sum(newNums)   #smaller value
        return expectedSum-actualSum
