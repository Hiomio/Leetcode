class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        '''
        bfs to find safeness factor of each cell
        greedy + heap -> choose path with max safeness factor
        '''
        # bfs
        n = len(grid)
        queue = deque() # deque of (i, j, dist)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
        factors = [[-1] * n for _ in range(n)]

        while queue:
            for _ in range(len(queue)):
                curi, curj, dist = queue.popleft()
                if not (0 <= curi < n and 0 <= curj < n): # exceed grid
                    continue
                if factors[curi][curj] != -1: # seen
                    continue
                factors[curi][curj] = dist
                for ii, jj in [[1,0],[-1,0],[0,-1],[0,1]]:
                    queue.append((curi + ii, curj + jj, dist + 1))
        
        # greedy + heap -> find ans
        heap = [[-factors[0][0], 0, 0]] # heap of [-safeness_factor, i, j]
        seen = set()

        while heap:
            fac, i, j = heapq.heappop(heap)
            fac *= -1
            if i == j == n - 1: # reach ans
                return fac
            if (i, j) in seen: # seen
                continue
            seen.add((i, j))

            for ii, jj in [[1,0],[-1,0],[0,-1],[0,1]]:
                ni, nj = i + ii, j + jj
                if not (0 <= ni < n and 0 <= nj < n): # exceed grid
                    continue
                heapq.heappush(heap, [-min(fac, factors[ni][nj]), ni, nj])
        
        return -1
            