class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 0:
            mid = len(s) // 2
            openBracketHalf = s[:mid]
            closedBracketHalf = s[mid:]
        else:
            return False

        for bracket in closedBracketHalf:
            open = openBracketHalf[-1]
            openBracketHalf = openBracketHalf[:-1]
            close = bracket
            print("O", open)
            print("C", close)
            fullBracket = open + close
            if fullBracket not in ["{}", "[]", "()"]:
                return False
        return True
            
