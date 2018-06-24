class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) <= 1:
            return s

        length = len(s)
        res = s[0]
        dp = [[0 for i in range(length)] for i in range(length)]
        for i in range(length-1,-1,-1):
            for j in range(i+1,length):
                dp[i][j] = s[i] == s[j] and (dp[i+1][j-1] or j-i <= 2)
                if dp[i][j] and (not res or len(res) < j-i+1):
                    res = s[i:j+1]
        return res
    # 'a'-> 'a'
    # 'aa' -> 'aa'
    # 'abcd' -> 'a'
