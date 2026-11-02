class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans=[]
        #for i in range(len(nums)):
        #    ans.append(nums[i])
        #ans += ans
        ans = nums+nums
        return ans 