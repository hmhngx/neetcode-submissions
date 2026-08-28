class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        
        max_reach = 0 # max steps can reach

        for i in range(len(nums)):
            # if index > max can reach --> False
            if i > max_reach:
                return False
            
            # update max steps can reach: start at new steps of each idx or extend current one
            max_reach = max(max_reach, nums[i] + i)

            # if can reach end or beyond: true
            if max_reach >= len(nums) - 1:
                return True
        
        return False