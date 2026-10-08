"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()
        i = 0
        j = 0
        count = 0
        maxCount = 0
        while (i < len(starts)):
            if(starts[i] < ends[j]):
                i += 1
                count += 1
                maxCount = max(count, maxCount)
            else:
                j += 1
                count -= 1
        return maxCount