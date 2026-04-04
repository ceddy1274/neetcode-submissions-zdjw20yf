class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        obj = {}
        n = len(nums)

        for num in nums:
            tmp = int(num/(n+1))
            try:
                obj[tmp].add(num)
            except KeyError:
                obj[tmp] = set()
                obj[tmp].add(num)
        maxi = -1
        for lis in obj:
            tmp = len(obj[lis])
            if tmp > maxi:
                maxi = tmp


        return maxi