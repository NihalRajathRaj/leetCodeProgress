class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans=[]
        n=len(nums)
        for i in range(n):
            ans.append(nums[i])
        ans += ans
        return ans