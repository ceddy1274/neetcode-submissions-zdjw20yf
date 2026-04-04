import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
       cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s)
       if(len(cleaned_string) <= 1):
        return True
        
       start = 0
       end = len(s)-1
       while(start <= end):
            while(not s[start].isalnum()):
                start += 1
            while(not s[end].isalnum()):
                end -= 1
            if(s[start].lower() != s[end].lower()):
                return False
            start += 1
            end -= 1
       return True