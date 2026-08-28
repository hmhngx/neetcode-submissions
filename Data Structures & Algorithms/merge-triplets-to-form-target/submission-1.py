class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if not triplets and not target:
            return True
        
        x, y, z = target
        a, b, c = 0, 0, 0

        for triplet in triplets:
            tx, ty, tz = triplet

            if tx <= x and ty <= y and tz <= z:
                a = max(a, tx)
                b = max(b, ty)
                c = max(c, tz)
            
                if a == x and b == y and c == z:
                    return True
        
        return a == x and b == y and c == z