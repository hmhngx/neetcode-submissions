"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
    
        # Sort intervals by start time
        intervals.sort(key=lambda x: x.start)
        
        for i in range(1, len(intervals)):
            # If current meeting starts before previous meeting ends
            if intervals[i].start < intervals[i-1].end:
                return False
        
        return True