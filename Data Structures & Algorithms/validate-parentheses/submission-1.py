class Solution:
    def isSameBracket(self, open: str, close: str) -> bool:
        if open == "{" and close == "}":
            return True
        elif open == "[" and close == "]":
            return True
        elif open == "(" and close == ")":
            return True
        else:
            return False
    def isValid(self, s: str) -> bool:
        # Return true if:
        # 1) Every open bracket is closed by same type of closed bracket
        # 2) Open brackets are closed in the correct order
        # 3) Every close bracket has a corresponding open bracket of the same type

        # Return false for uneven string
        if len(s) % 2 != 0:
            return False
        # IDEA: Loop through half the string until you find a closing bracket. Once you find it,
        # begin popping off the stack.
        stack = []
        for bracket in s:
            if bracket in ['}', ')', ']']:
                if len(stack) < 0:
                    return False
                open = stack.pop()
                close = bracket
                if(self.isSameBracket(open, close)) == False:
                    return False
            else:
                stack.append(bracket)
        return True
                
            