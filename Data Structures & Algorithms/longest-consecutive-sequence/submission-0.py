class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        obj = {}
        n = len(nums)

        for num in nums:
            tmp = int(num/n)
            try:
                obj[tmp].add(num)
            except KeyError:
                obj[tmp] = set()
                obj[tmp].add(num)
        maxi = -1
        print(obj)
        for lis in obj:
            tmp = len(obj[lis])
            if tmp > maxi:
                maxi = tmp


        return maxi