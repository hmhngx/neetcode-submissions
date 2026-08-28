class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # length of the nums arr
        n = len(nums)

        # ans array to store values from nums 
        # init with size 2*n
        ans = [0] * (2*n)
        
        # loop thru the nums arr
        for i in range(n):
            # write value of each idx in nums to ans[i] and ans[i + n]
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        
        return ans

        # time: O(n)
        # space: O(n)