class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1
        oneZero = False
        for num in nums:
            if num == 0 and not oneZero:
                oneZero = True
            else:
                prod *= num
        for num in nums:
            if oneZero and num != 0:
                res.append(0)
            elif oneZero:
                res.append(prod)
            else:
                try:
                    res.append((int)(prod/num))
                except ZeroDivisionError:
                    res.append(prod)
        return res