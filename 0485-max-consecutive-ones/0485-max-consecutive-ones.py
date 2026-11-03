class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count=0
        longest=0
        for i in nums:
            if(i==1):
                count +=1
                longest=max(count, longest)
            else:
                count=0
        return longest


