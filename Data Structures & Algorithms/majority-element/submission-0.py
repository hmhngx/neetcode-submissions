class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # edge case
        if not nums:
            return None
        
        # init major elem and its counter
        major = None
        count = 0

        # loop thru the array nums
        for num in nums:
            # move the major elem to another elem in nums if count reaches 0
            # replace the major elem
            if count == 0:
                major = num
            
            # add up to the counter of major elem if the next number in nums match it 
            # or else decrease
            count += (1 if num == major else -1)
        
        return major

        # time: O(n) -> 1 pass thru the array
        # space O(1) -> only uses 2 tracking elems regardless of the array input size