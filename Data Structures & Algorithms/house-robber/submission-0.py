class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        prev2, prev1 = 0, 0

        for num in nums:
            current = max(num + prev2, prev1)
            prev2, prev1 = prev1, current
        

        return prev1