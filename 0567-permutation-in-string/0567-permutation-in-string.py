from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need=Counter(s1)
        existing=Counter()
        left=0
        for right in range(len(s2)):
            existing[s2[right]]=existing.get(s2[right],0)+1
            while right - left + 1 > len(s1):
                existing[s2[left]]-=1
                if existing[s2[left]]==0 :
                    del existing[s2[left]] 
                left+=1
            if existing==need:
                return True         
        return False
