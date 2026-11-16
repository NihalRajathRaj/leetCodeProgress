class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:]
        N=n.zfill(32)
        revN = N[::-1]
        return int(revN, 2)