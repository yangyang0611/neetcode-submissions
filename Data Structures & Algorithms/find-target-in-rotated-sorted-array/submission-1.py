class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right-left)//2

            if nums[mid] == target:
                return mid

            elif nums[left] <= nums[mid]: # mid屬於左半邊嗎
                if nums[left] <= target < nums[mid]: # 在左半邊
                    right = mid - 1
                else: # 在右半邊
                    left = mid + 1

            elif nums[mid] <= nums[right]: # mid屬於右半邊嗎
                if nums[mid] < target <= nums[right]: # 在右半邊
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1