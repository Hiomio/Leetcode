class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        degree = [0] * n
        edge = [[] for _ in range(n)]
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            edge[u].append(v)
            edge[v].append(u)
        
        vis = [False] * n
        ans = 0
        
        for i in range(n):
            if vis[i]:
                continue
            curr = []
            st = [i]
            vis[i] = True
            
            while st:
                u = st.pop()
                curr.append(u)
                for v in edge[u]:
                    if not vis[v]:
                        st.append(v)
                        vis[v] = True
            
            ok = True
            for u in curr:
                if degree[u] != len(curr) - 1:
                    ok = False
                    break
            
            if ok:
                ans += 1
                
        return ans