class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_chars = set()
        longest_string = 0
        setter = 0
        while(setter < len(s)):
            current_chars.add(s[setter])
            mover = setter + 1
            while(mover < len(s) and s[mover] not in current_chars):
                current_chars.add(s[mover])
                mover += 1
            current_length = mover - setter
            longest_string = max(longest_string, current_length)
            current_chars = set()
            setter += 1

        return longest_string

