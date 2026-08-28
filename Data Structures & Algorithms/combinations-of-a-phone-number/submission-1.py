class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digitsMap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        res = []

        def backtrack(idx, path):
            if idx == len(digits):
                return res.append(''.join(path))

            currDigits = digits[idx]
            for letters in digitsMap[currDigits]:
                path.append(letters)
                backtrack(idx + 1, path)
                path.pop()
        
        backtrack(0, [])
        return res