class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = max(nums)
        n = len(nums)
        result = 0

        for i in range(n+1):
            if i not in nums:
                print(i)
                return i
        return 0