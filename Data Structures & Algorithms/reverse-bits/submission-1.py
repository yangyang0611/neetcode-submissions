class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:].zfill(32)
        reverse = n[::-1]
        return int(reverse, 2)
