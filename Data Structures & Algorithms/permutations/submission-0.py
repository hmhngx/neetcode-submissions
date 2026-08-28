class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, visited):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if not visited[i]:
                    path.append(nums[i])
                    visited[i] = True
                    backtrack(path, visited)
                    path.pop()
                    visited[i] = False
        
        backtrack([], [False] * len(nums))
        return res