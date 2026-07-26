class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(bigger, smaller):
            if (bigger-smaller) == 0:
                return bigger
            i = 1
            j = 1
            iTurn = False
            newNum = bigger*i - smaller*j
            while(newNum > smaller):
                if iTurn:
                    i += 1
                    newNum = bigger*i - smaller*j
                else:
                    j += 1
                    newNum = bigger*i - smaller*j
            return gcd(smaller, newNum)
        
        bigger = max(len(str1), len(str2))
        smaller = min(len(str1), len(str2))
        length = gcd(bigger, smaller)

        divisor = str1[:length]
        i = length
        j = i + length
        while(j <= len(str1)):
            curr = str1[i:j]
            if curr != divisor:
                return ""
            i += length
            j += length
        i = 0
        j = length
        while(j <= len(str2)):
            curr = str2[i:j]
            if curr != divisor:
                return ""
            i += length
            j += length
        return divisor

            