class Solution:
    def searchIndexOfMinElement(self, nums):
        if nums[0] <= nums[-1]: # already sorted
            return 0
        
        left = 1
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid-1] > nums[mid]:
                return mid
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    def binarySearch(self, nums, target, left, right):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        pivot = self.searchIndexOfMinElement(nums)
        if target <= nums[-1]:
            return self.binarySearch(nums, target, pivot, len(nums) - 1)
        return self.binarySearch(nums, target, 0, pivot - 1)