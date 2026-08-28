class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        def linear(nums: List[int]) -> int:
            prev2, prev1 = 0, 0
            for num in nums:
                prev2, prev1 = prev1, max(prev2 + num, prev1)

            return prev1
        

        return max(linear(nums[:-1]), linear(nums[1:]))