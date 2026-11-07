class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        def happy(n):
            sum = 0
            for i, digit in enumerate(str(n)):
                sum += (int(digit)) ** 2
            return sum

        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            n = happy(n)
        return True
