class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right-left)//2
            if nums[mid] <= nums[right]:
                right = mid  # 因爲mid比right小，表示最小值在左邊，而有可能mid就是最小的
            elif nums[mid] > nums[right]:
                left = mid + 1
        
        return nums[left] # return nums[right]