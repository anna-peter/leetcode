class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # start at -1
        # step +1 or +2
        # finish at len(cost)
        # recursive -> start at the finish and its max(finish -1,finish -2)
        #dp[i] = cost to reach i
        dp = [0]*len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        # dp[2] = min(dp[0]+cost[2], dp[1])
        # dp[3] = min(dp[0]+dp[1]+cost[3], dp[0]+cost[2], dp[1]+cost[3],)
        for i in range(2,len(cost)):
            dp[i] = min(dp[i-2]+cost[i], dp[i-1]+cost[i]) # condition: either we stepped from i-2 or i-1
        return min(dp[-1],dp[-2])