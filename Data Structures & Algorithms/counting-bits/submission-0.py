from collections import Counter
class Solution:
    def countBits(self, n: int) -> List[int]:
        count = 0
        result = [0] * (n + 1)
        for i in range(n+1):
            current = bin(i)[2:]
            print(current)
            c = Counter(current)
            print(c)
            count = c["1"]
            result[i] = count
            print(result)
        return result