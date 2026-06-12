class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges)+1
        parents = list(range(n+1))    

        for u, v in edges:
            if u<v:
                parents[v] = u
            else:
                parents[u] = v

        depths = [-1]*(n+1)
        depths[1] = 0

        def get_depth(node):
            if depths[node]==-1:
                depths[node] = get_depth(parents[node])+1
            return depths[node]

        @cache
        def solve(u, v):
            du = get_depth(u)
            dv = get_depth(v)
            res = 0
            while du<dv:
                v = parents[v]
                dv-=1
                res+=1
            while dv<du:
                u = parents[u]
                du-=1
                res+=1
            if u==v:
                return res
            # much more chances that same depth is already cached
            return 2+res+solve(parents[u], parents[v])

        res = []
        for u, v in queries:
            if u==v:
                res.append(0)
                continue
            res.append(pow(2, solve(u, v)-1, 1_000_000_007))
        return res