class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Longest subsequence, while ignoring k characters
        l = 0
        res = 0
        alphaSet = {}
        for r in range(len(s)):
            try:
                alphaSet[r] += 1
            except KeyError:
                alphaSet[r] = 1
            maxFreak = 0
            for alpha in alphaSet:
                maxFreak = max(maxFreak, alphaSet[alpha])
            diff = (r)-l - maxFreak
            if(diff <= k):
                res = max(res, (r-l))
            else:
                l += 1
        return res
        

        

        