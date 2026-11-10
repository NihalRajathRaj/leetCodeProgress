class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        n = x
        while True:
            root = (n + x // n) // 2
            if root >= n:
                return n
            n = root
