from collections import Counter
class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n).zfill(32)
        c = Counter(n)
        print(c)
        count = 0
        count = c["1"]
        return count