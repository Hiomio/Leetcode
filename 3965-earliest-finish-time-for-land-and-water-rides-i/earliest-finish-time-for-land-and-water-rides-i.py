class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n: int = len(landStartTime)
        m: int = len(waterStartTime)
        output: int = float('inf')
        for i in range(n):
            for j in range(m):
                x: int = landStartTime[i] + landDuration[i]
                y: int = waterStartTime[j] + waterDuration[j]
                if x <= waterStartTime[j]: output = min(output, y)
                else: output = min(output, x + waterDuration[j])
                if y <= landStartTime[i]: output = min(output, x)
                else: output = min(output, y + landDuration[i])
        return output