import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        min_coin = min(coins)
        max_limit = min_coin * k
        
        subsets = []
        
        # Step 1: Precompute all valid subset LCMs and their sign (+1 or -1)
        for mask in range(1, 1 << n):
            current_lcm = 1
            bit_count = 0
            overflow = False
            
            for i in range(n):
                if mask & (1 << i):
                    bit_count += 1
                    current_lcm = math.lcm(current_lcm, coins[i])
                    if current_lcm > max_limit:
                        overflow = True
                        break
            
            if not overflow:
                sign = 1 if bit_count % 2 == 1 else -1
                subsets.append((current_lcm, sign))
        
        # Step 2: Binary Search with O(len(subsets)) lookup
        left, right = 1, max_limit
        ans = right

        while left <= right:
            mid = (left + right) // 2
            
            # Count multiples <= mid
            total_count = sum(sign * (mid // lcm_val) for lcm_val, sign in subsets)
            
            if total_count >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans