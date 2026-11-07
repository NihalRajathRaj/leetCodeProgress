class Solution:
    def repeatedCharacter(self, s: str) -> str:
        visited = set()
        for i, ch in enumerate(s):
            if ch not in visited:
                visited.add(s[i])
            else:
                return ch
