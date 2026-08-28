class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(remain, start, path):
            if remain == 0:
                res.append(list(path))
                return
            
            for i in range(start, len(nums)):
                if nums[i] > remain:
                    break
                path.append(nums[i])
                backtrack(remain - nums[i], i, path)
                path.pop()
        backtrack(target, 0, [])
        return res
