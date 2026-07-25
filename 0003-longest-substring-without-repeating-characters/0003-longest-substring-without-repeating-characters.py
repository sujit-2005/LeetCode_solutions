class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        max_length=0
        left=0
        ss=""
        for right in range(len(s)):
            ss+=s[right]
            while len(set(ss))!=len(ss) and left<right:
                ss=ss[1:]
            length=len(ss)
            max_length=max(length,max_length)
        return max_length