class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        currMax = currMin = res = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]

            if curr < 0:
                currMax, currMin = currMin, currMax
            
            currMax = max(curr, curr * currMax)
            currMin = min(curr, curr * currMin)

            res = max(res, currMax)
        
        return res

