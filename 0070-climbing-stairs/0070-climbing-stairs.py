class Solution:
    def climbStairs(self, n: int) -> int:
        # build arr dp[] where dp[i] defines the number of ways to climb i steps
        # solution will be dp[n]
        # we build dp from the bottom up (more efficient)
        if n <=2:
            return n
        dp = [0]*n
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i-1]+dp[i-2]
       # dp[3] = dp[2] + dp[1] = 3
       # dp[4] = 3 + 2 = 5 # 1,1,1,1 - 1,2,1 - 1,1,2 -2,2 - 2,1,1 
        return dp[n-1]