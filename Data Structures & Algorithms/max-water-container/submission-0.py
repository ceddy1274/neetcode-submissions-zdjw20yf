class Solution:
    def maxArea(self, heights: List[int]) -> int:
        distinct = set(heights)
        maxi1 = max(distinct)
        distinct.remove(maxi1)
        try:
            maxi2 = max(distinct) 
            return (maxi2*maxi2)
        except ValueError:
            return (maxi1*maxi1)