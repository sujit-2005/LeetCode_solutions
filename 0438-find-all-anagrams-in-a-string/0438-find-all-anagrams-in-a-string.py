from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d=[]
        left=0
        need=Counter(p)
        existing=Counter()
        for right in range(len(s)):
            existing[s[right]]=existing.get(s[right],0)+1
            while right-left+1>len(p):
                existing[s[left]]-=1
                if existing[s[left]]==0:
                    del existing[s[left]]
                left+=1
            if existing==need:
                d.append(left)
            
        return d