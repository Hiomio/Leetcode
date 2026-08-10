class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # recursive leap of faith
        dp: list[bool | None] = [None] * (n+1)

        # this rec call is for alice
        return self.solve(n, dp)

    def solve(self, n: int, dp: list[bool | None]) -> bool:
        if n == 0:
            # if n==0 than who so ever is here will loose
            return False

        if dp[n] is not None:
            return dp[n]

        i: int = 1
        while i <= int(sqrt(n)):
            # bob did you win? if false than alice win
            if self.solve(n-i*i, dp) is False:
                dp[n] = True
                return True

            i += 1

        dp[n] = False
        return False

        