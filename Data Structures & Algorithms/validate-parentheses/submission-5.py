class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        currentIteration = 1
        for bracket in s:
            if bracket in ["}", "]", ")"]:
                if len(stack) == 0:
                    return False
                open = stack.pop()
                close = bracket
                fullBracket = open + close
                if fullBracket not in ["{}", "[]", "()"]:
                    return False
                elif currentIteration == len(s):
                    return True 
            else:
                stack.append(bracket)
            currentIteration += 1

            
