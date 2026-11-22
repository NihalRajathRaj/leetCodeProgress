class Solution:
    def checkString(self, s: str) -> bool:
        i = 0
        while i < len(s):
            if s[i] == 'b':
                s = s[i:]
                if 'a' in s:
                    return False
            i += 1
        return True