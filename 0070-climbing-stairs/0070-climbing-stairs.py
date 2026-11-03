class Solution:
    def climbStairs(self, n: int) -> int:
        result=n
        if n<=3:
            return result
        a=2
        b=3
        for i in range(4, n+1):
            result=a+b
            a=b
            b=result
        return result