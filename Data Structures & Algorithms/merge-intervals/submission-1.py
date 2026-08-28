class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])

        res = []
        curr_interval = intervals[0]

        for i in range(1, len(intervals)):
            next_interval = intervals[i]

            # check overlap 
            if curr_interval[1] >= next_interval[0]:
                curr_interval[1] = max(curr_interval[1], next_interval[1])
            else:
                res.append(curr_interval)
                curr_interval = next_interval
        
        res.append(curr_interval)
        return res