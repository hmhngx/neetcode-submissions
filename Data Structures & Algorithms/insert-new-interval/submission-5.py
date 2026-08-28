class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals and not newInterval:
            return []
        
        i = 0
        n = len(intervals)
        res = []

        # non overlap intervals: end of origin < start of new
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # overlapping intervals: start of old before or at the end new
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # the rest
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res
