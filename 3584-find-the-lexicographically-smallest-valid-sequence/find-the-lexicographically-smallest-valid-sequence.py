class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        m, n = len(word1), len(word2)
        right_match = [-1] * n
        
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                right_match[j] = i
                j -= 1
            i -= 1
            
        res = []
        i = j = 0
        changed = False
        
        while i < m and j < n:
            if word1[i] == word2[j]:
                res.append(i)
                j += 1
            elif not changed and (j == n - 1 or right_match[j + 1] > i):
                changed = True
                res.append(i)
                j += 1
            i += 1
            
        return res if j == n else []