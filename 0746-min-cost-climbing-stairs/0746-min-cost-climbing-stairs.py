class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costs = {}
        costs[0] = 0
        costs[1] = 0
        
        for i in range(2, len(cost) + 1):
            costs[i] = min(costs.get(i - 1) + cost[i - 1], costs.get(i - 2) + cost[i - 2])
             
        return costs[len(cost)]