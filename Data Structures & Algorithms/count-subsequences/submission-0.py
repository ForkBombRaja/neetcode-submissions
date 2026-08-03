class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Empty target can always be formed
        for i in range(n + 1):
            dp[i][m] = 1

        # Fill from bottom-right
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]

        return dp[0][0]
