# Last updated: 5/6/2025, 11:09:52 pm
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        # Handle empty string edge case
        if n == 0:
            return 0
        
        # DP array initialization
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: an empty string has one way to be decoded
        
        # A single character string can be decoded if it is not '0'
        dp[1] = 1 if s[0] != '0' else 0
        
        for i in range(2, n + 1):
            one_digit = int(s[i-1:i])  # Single digit
            two_digit = int(s[i-2:i])  # Two digits
            
            # Check if the single digit is valid (1-9)
            if 1 <= one_digit <= 9:
                dp[i] += dp[i-1]
            
            # Check if the two-digit number is valid (10-26)
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]


