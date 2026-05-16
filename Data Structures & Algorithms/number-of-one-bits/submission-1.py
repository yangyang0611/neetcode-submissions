from collections import Counter
class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n).zfill(32)
        c = Counter(n)
        return c["1"]