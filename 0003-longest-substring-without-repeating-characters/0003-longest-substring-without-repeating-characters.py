class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        t = ""
        result = 0
        for ch in s:
            if ch not in t:
                t += ch
                result = max(result, len(t))
            else:
                while ch in t:
                    t = t[1:]
                t += ch
                result = max(result, len(t))
        return result
