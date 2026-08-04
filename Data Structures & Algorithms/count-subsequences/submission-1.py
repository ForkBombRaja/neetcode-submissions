class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # get lenths of each string
        sLength, tLength = len(s), len(t)
        # get a frame
        dp = [[0] * (tLength + 1) for char in range(sLength + 1)]
        for char in range(sLength + 1):
            '''
            Get each char for t length
            '''
            dp[char][tLength] = 1
        for i in range(sLength - 1, -1, -1):
            '''
            for each in s  go on t
            '''
            for j in range(tLength - 1, -1, -1):
                '''
                for each potential check chars 
                else reset 
                '''
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]
        return dp[0][0]
