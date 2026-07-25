class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0 
        uniset = set()
        max_len = 0
        for r in range(n):
            ch = s[r]
            if ch not in uniset:
                uniset.add(ch)
            else:
                while ch in uniset:
                    uniset.remove(s[l])
                    l += 1
            uniset.add(s[r])
            max_len = max(max_len, len(uniset))
        
        return max_len