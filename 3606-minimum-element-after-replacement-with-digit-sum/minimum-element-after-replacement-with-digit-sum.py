class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float('inf')

        for num in nums:
            digit_sum = 0
            temp = num

            while temp > 0:
                digit_sum += temp % 10
                temp //= 10

            ans = min(ans, digit_sum)

        return ans