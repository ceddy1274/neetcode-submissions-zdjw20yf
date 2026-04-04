class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        curr_last = len(first_word) - 1
        same = True
        for i in range(1, len(strs)):
            if(same and strs[i] != strs[0]):
                same = False
            while(curr_last < len(strs[i]) and curr_last < len(first_word) and
            strs[i][curr_last] != first_word[curr_last]):
                first_word = first_word[:curr_last]
                curr_last -= 1 
        if(not(same) and len(first_word) == len(strs[0])):
            return ""
        return first_word