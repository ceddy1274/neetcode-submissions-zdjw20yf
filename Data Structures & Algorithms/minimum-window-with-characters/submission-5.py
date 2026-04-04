class Solution:
    def findLength(self, possibleLengths):
        pass

    def minWindow(self, s: str, t: str) -> str:
        l = 0
        minLength = float('inf')
        minSubstring = ""
        if(len(t) > len(s)):
            return minSubstring
        
        
        r = len(s) 
        tSet = set(t)
        while(l < len(s)):
            currSubstringSet = set(s[l:r])
            if(len(tSet - currSubstringSet) == 0 and len(s[l:r]) < minLength):
                minSubstring = s[l:r]
                minLength = len(s[l:r])
            l += 1
        l = 0
        while(r >= 0):
            currSubstringSet = set(s[l:r])
            if(len(tSet - currSubstringSet) == 0 and len(s[l:r]) < minLength):
                minSubstring = s[l:r]
                minLength = len(s[l:r])
            r -= 1
        l = 0
        r = len(minSubstring) - 1
        # while(minSubstring[l] not in t):
        #     l += 1
        while(minSubstring[r] not in t):
            r -= 1
        

        
        return minSubstring

        
