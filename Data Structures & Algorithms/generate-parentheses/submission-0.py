class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(openCount, closeCount, path):
            if openCount == n and closeCount == n:
                res.append("".join(path))
                return

            if openCount < n:
                path.append("(")
                helper(openCount + 1, closeCount, path)
                path.pop()
            
            if closeCount < openCount:
                path.append(")")
                helper(openCount, closeCount + 1, path)
                path.pop()
        
        helper(0, 0, [])
        return res