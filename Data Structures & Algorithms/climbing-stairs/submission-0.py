class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        one, two = 1, 1

        for i in range(2, n + 1):
            one, two = two, one + two
        
        return two