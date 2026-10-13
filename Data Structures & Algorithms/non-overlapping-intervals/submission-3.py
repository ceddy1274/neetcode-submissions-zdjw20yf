class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda intervals: intervals[1])
        currEnd = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < currEnd:
                count += 1
            else:
                currEnd = intervals[i][1]
            

        return count