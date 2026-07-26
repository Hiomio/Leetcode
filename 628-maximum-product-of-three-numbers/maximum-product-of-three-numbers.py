class Solution:
    def maximumProduct(self, a: List[int]) -> int:
        return max(prod(nlargest(3,a)),prod(nsmallest(2,a))*max(a))