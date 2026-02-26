import math
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        
        count = 0
        
        # process from last parent to root
        for i in range(n//2 - 1, -1, -1):
            left = 2*i + 1
            right = 2*i + 2
            
            diff = abs(cost[left] - cost[right])
            count += diff
            
            # propagate max path upward
            cost[i] += max(cost[left], cost[right])
        
        return count