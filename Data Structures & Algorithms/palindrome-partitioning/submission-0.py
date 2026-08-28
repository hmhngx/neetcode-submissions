class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalin(subs: str) -> bool:
            return subs == subs[::-1]
        
        def backtrack(start, path):
            if start == len(s):
                return res.append(path.copy())

            for end in range(start + 1, len(s) + 1):
                subStr = s[start:end]
                if isPalin(subStr):
                    path.append(subStr)
                    backtrack(end, path)
                    path.pop()
        
        backtrack(0, [])
        return res