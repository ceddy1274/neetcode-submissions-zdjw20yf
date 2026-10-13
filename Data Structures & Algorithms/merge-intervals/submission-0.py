class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      intervals = sorted(intervals, key=lambda intervals: intervals[0])
      print(intervals)
      currEnd = intervals[0][1]
      newIntervals = [intervals[0]]
      currIndexOfNewIntervals = 0
      for i in range(1, len(intervals)):
        if intervals[i][0] <= currEnd and intervals[i][1] > currEnd:
            currEnd = intervals[i][1]
            newIntervals[currIndexOfNewIntervals][1] = currEnd
        elif intervals[i][0] > currEnd:
            newIntervals.append(intervals[i])
            currIndexOfNewIntervals += 1
            currEnd = intervals[i][1]
      return newIntervals