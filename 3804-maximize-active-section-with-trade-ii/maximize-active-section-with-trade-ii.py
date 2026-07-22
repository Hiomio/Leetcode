class SparseTable:
    def __init__(self, arr):
        self.n, self.t = len(arr), [arr[:]]
        for p in range(1, self.n.bit_length()):
            self.t.append(list(map(max, self.t[-1], self.t[-1][1<<(p-1) :])))
            
    def query(self, lft, rgt):
        if  lft >= rgt:  return 0
        p = (rgt - lft).bit_length()-1
        return  max(self.t[p][lft], self.t[p][rgt - (1<<p)])


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        zeros = [(m.end()-1, m.start()) for m in re.finditer(r'0+',s)]
        ans   = [s.count('1')] *len(queries)
        st    = SparseTable([sum(starmap(sub, pair)) +2 for pair in pairwise(zeros)])
        for i,(l,r) in enumerate(queries):
            lz,rz = bisect_left(zeros,(l,0)), bisect_left(zeros,(r,0))
            rz   -= (rz >= len(zeros)) or (r < zeros[rz][1])
            if  rz > lz:  ans[i] += max(
                zeros[lz][0] -max(l, zeros[lz][1]) + min(r, zeros[lz+1][0]) -zeros[lz+1][1] + 2,
                zeros[rz-1][0] -max(l, zeros[rz-1][1]) + min(r, zeros[rz][0]) -zeros[rz][1] + 2,
                st.query(lz+1, rz-1)
            )
        return  ans
        