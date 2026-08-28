"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # edge case
        if not intervals:
            return 0
        
        # sort start, end times separately
        start_time = sorted([i.start for i in intervals])
        end_time = sorted([i.end for i in intervals])

        # pointers
        start, end = 0, 0
        max_room = 0
        need_room = 0

        for i in range(start, len(intervals)):
            if start_time[start] < end_time[end]:
                start += 1
                need_room += 1
            else:
                end += 1
                need_room -= 1
            
            max_room = max(max_room, need_room)
    
        return max_room
                