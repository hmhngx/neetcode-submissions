class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # base case
        if not intervals:
            return []
        
        # sort the list
        intervals.sort(key=lambda x: x[0])

        res = []
        # start with the first interval in list
        curr_interval = intervals[0]
        
        for i in range(1, len(intervals)):
            next_interval = intervals[i]

            # check if overlap (curr_end >= next_start):
            if curr_interval[1] >= next_interval[0]:
                # merge
                curr_interval[1] = max(next_interval[1], curr_interval[1])
            
            else:
                res.append(curr_interval)
                # move forward
                curr_interval = next_interval
            
        # add last interval
        res.append(curr_interval)
        return res