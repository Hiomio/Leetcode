class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()

        missing = []

        for i in range(len(nums) - 1):
            current = nums[i]
            next_num = nums[i + 1]

            while current + 1 < next_num:
                current = current + 1
                missing.append(current)

        return missing