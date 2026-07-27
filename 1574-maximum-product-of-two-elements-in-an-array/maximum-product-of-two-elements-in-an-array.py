class Solution:
    def maxProduct(self, nums: List[int]) -> int:
     max=0
     n=len(nums)
     for i in range(n):
        for j in range(n):
            if i!=j:
                v=(nums[i]-1 )* (nums[j]-1)
                if v>max:
                    max=v
     return max
            