from collections import Counter
from itertools import islice
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        result = []

        sort = sorted(c.items(), key=lambda x:x[1], reverse=True)
        print(sort)
        for key, value in islice(sort, k):
            result.append(key)
        return result