class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        for key, val in freq.items():
            if val == 1:
                return key