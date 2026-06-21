class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        c,i = 0,0
        if costs[0] > coins:
            return c
        while i < len(costs):
            if costs[i] <= coins:
                coins -= costs[i]
                c += 1
            i+=1
        return c
        