class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        v = "aeiou"
        c = 0

        for l in s[:k]:
            if l in v:
                c += 1
        
        maxV = c

        for i in range(k,len(s)):
            if s[i] in v:
                c += 1
            
            if s[i-k] in v:
                c -= 1

            if c > maxV:
                maxV = c
        
        return maxV