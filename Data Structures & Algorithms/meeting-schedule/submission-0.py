"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        def sortKey(interval):
            return interval.start
        intervals.sort(key=sortKey)
        print(intervals)
        for i in range(len(intervals)-1):
            currEnd = intervals[i].end
            nextStart = intervals[i+1].start
            if nextStart < currEnd:
                return False
        return True