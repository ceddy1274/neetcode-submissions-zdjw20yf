class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Longest subsequence, while ignoring k characters
        l = 0
        res = 0
        alphaSet = {}
        for r in range(len(s)):
            try:
                alphaSet[s[r]] += 1
            except KeyError:
                alphaSet[s[r]] = 1
            maxFreak = 0
            for alpha in alphaSet:
                maxFreak = max(maxFreak, alphaSet[alpha])
            print(alphaSet)
            print("Freak:", maxFreak)
            print("R", r)
            print("L", l)
            diff = (r+1)-l - maxFreak
            if(diff <= k):
                res = max(res, ((r+1)-l))
            else:
                alphaSet[s[l]] -= 1
                l += 1

        return res
        

        

        