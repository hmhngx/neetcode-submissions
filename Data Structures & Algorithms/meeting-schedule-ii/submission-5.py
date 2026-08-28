"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        start_time = sorted(i.start for i in intervals)
        end_time = sorted(i.end for i in intervals)

        s, e = 0, 0
        need = 0
        max_room = 0

        for i in range(s, len(intervals)):
            if start_time[s] < end_time[e]:
                need += 1
                s += 1
            else:
                e += 1
                need -= 1
        
            max_room = max(max_room, need)
        
        return max_room
