class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # global max
        max_sum = nums[0]
        # local max
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            # update the current max: start new or extend current subarr
            curr_sum = max(nums[i], nums[i] + curr_sum)

            max_sum = max(max_sum, curr_sum)

        
        return max_sum