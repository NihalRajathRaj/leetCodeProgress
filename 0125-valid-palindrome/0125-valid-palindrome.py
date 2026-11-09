class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        S = "".join(ch for ch in s if ch.isalnum())
        l = 0
        r = len(S) - 1
        while l < r:
            if S[l] == S[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
