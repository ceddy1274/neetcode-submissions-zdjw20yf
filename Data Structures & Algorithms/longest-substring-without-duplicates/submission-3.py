class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_chars = set()
        longest_string = 0
        setter = 0
        mover = 1
        while(setter < len(s)):
            current_chars.add(s[setter])
            while(mover < len(s) and s[mover] not in current_chars):
                current_chars.add(s[mover])
                mover += 1
            current_length = len(current_chars)
            longest_string = max(longest_string, current_length)
            current_chars.remove(s[setter])
            setter += 1

        return longest_string
        

