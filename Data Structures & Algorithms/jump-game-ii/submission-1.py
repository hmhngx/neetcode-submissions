class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        jump = 0
        curr_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, nums[i] + i)

            if i == curr_end:
                jump += 1
                curr_end = farthest
            
            if curr_end >= len(nums) - 1:
                return jump
        
        return jump