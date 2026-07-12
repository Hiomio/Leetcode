class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(set(arr))
        rank_map = {}
        res = []
        for i in range(0, len(temp)):
            if temp[i] not in rank_map:
                rank_map[temp[i]] = i + 1
        

        for j in arr:
            res.append(rank_map[j])
            
        return res