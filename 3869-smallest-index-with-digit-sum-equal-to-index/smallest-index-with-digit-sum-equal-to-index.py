class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        def calc_digit_sum(num: int) -> int:
            total_sum = 0
            while num > 0:
                # Extract lowest base-10 digit to accumulate total numeric value sum.
                num, rem = divmod(num, 10)
                total_sum += rem
            return total_sum
            
        # 1. Map sequence values to their zero-based positions for simultaneous evaluation.
        # 2. Scan linearly to find the earliest occurrence where position equals digit sum.
        for idx, num in enumerate(nums):
            if idx == calc_digit_sum(num):
                # 3. Resolve the underlying index if found, or yield missing state.
                return idx
                
        return -1