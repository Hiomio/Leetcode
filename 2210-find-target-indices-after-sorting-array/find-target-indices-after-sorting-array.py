
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lt = eq = 0
        for x in nums:
            if x < target:
                lt += 1
            elif x == target:
                eq += 1
        return list(range(lt, lt + eq))