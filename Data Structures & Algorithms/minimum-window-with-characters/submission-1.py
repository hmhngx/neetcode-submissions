class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        need = {}
        window = {}
        left, right = 0, 0
        valid = 0
        start = 0
        minLen = float('inf')

        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        
        while right < len(s):
            char = s[right]
            right += 1

            if char in need:
                window[char] = window.get(char, 0) + 1
                if window[char] == need[char]:
                    valid += 1
            
            while valid == len(need):
                if right - left < minLen:
                    minLen = right - left
                    start = left
                
                left_char = s[left]
                left += 1

                if left_char in need:
                    if window[left_char] == need[left_char]:
                        valid -= 1
                    window[left_char] -= 1
        
        return s[start: start + minLen] if minLen != float('inf') else ""