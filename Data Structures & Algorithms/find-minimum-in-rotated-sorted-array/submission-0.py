class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]: # min在右邊
                left = mid + 1
            else: # min在左邊
                right = mid
        return nums[left]