class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        prev2, prev1 = 1, 1

        for i in range(1, len(s)):
            count = 0

            if s[i] != '0':
                count += prev1
            
            if 10 <= int(s[i-1:i+1]) <= 26:
                count += prev2
            
            prev2, prev1 = prev1, count
        
        return prev1