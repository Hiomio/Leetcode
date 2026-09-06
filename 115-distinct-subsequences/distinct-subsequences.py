class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m , n = len(s) , len(t)
        dp = [0] * (n+1)
        dp [-1] = 1
        for i in range(m-1,-1,-1):
            start = max(0, n - m + i)
            end = min(n - 1, i)
            for j in range(start, end + 1):
                if s[i] == t[j]:
                    dp[j] += dp[j + 1]
        return dp[0]