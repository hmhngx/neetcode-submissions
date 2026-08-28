class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start, path, remain):
            if remain == 0:
                res.append(path.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] > remain:
                    break
                
                path.append(candidates[i])

                backtrack(i + 1, path, remain - candidates[i])
                path.pop()
        
        backtrack(0, [], target)
        return res