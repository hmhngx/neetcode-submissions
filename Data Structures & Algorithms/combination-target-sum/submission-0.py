class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, remain):
            if remain == 0:
                res.append(path.copy())
                return


            for i in range(start, len(nums)):
                if nums[i] > remain:
                    continue
                
                path.append(nums[i])

                backtrack(i, path, remain - nums[i])

                path.pop()
        
        backtrack(0, [], target)
        return res
