class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ovl,stk = 0, []
        for a,b in sorted(intervals, key=lambda e: (e[0],-e[1])):
            while stk and a >= stk[-1]: stk.pop()
            if    stk and b <= stk[-1]: ovl += 1
            else:                       stk.append(b)
        return  len(intervals) - ovl
        