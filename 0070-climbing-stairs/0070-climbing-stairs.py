class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        
        steps = {}
        steps[1] = 1
        steps[2] = 2

        for i in range(3, n + 1):
            steps[i] = steps.get(i-1) + steps.get(i-2)
        
        return steps[n]