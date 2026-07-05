class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        m, n = len(board), len(board[0])
        mod = 10 ** 9 + 7
        @cache
        def dp1(i, j):
            if i < 0 or j < 0 or board[i][j] == 'X':
                return -inf
            if i == j == 0:
                return 0
            if board[i][j] != 'S':
                v = int(board[i][j])
            else:
                v = 0
            return v + max(
                dp1(i - 1, j - 1),
                dp1(i - 1, j),
                dp1(i, j - 1),
            )
        res1 = dp1(m - 1, n - 1)
        if res1 == -inf:
            return [0, 0]
        @cache
        def dp2(i, j, v):
            if i < 0 or j < 0 or board[i][j] == 'X':
                return 0
            if i == j == 0:
                return int(v == res1)
            if board[i][j] != 'S':
                v += int(board[i][j])
            res = 0
            if dp1(i - 1, j - 1) + v == res1:
                res += dp2(i - 1, j - 1, v)
                res %= mod
            if dp1(i - 1, j) + v == res1:
                res += dp2(i - 1, j, v)
                res %= mod
            if dp1(i, j - 1) + v == res1:
                res += dp2(i, j - 1, v)
                res %= mod
            return res
        res2 = dp2(m - 1, n - 1, 0)
        return [res1, res2]