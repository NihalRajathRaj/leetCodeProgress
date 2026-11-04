class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res=set(nums)
        for i in range(0,len(res)+1):
            if i not in res:
                return i
