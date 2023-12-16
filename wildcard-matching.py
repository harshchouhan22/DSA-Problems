
class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        # Create a 2D array to store the matching results
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        #Empty pattern matches empty string
        dp[0][0] = True

        #Handle patterns with '*' at the beginning 
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        #Populate the Dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # * can either match zero characters or one characters
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]
s = "aa"
p = "a"
result = Solution().isMatch(s, p)
print(result)
