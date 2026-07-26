class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need=[0]*26
        existing=[0]*26
        for char in s1:
            need[ord(char) - ord('a')] += 1
        left=0
        for right in range(len(s2)):
            existing[ord(s2[right])-ord('a')]+=1
            while right - left + 1 > len(s1):
                existing[ord(s2[left])-ord('a')]-=1
                left+=1
            if need==existing:
                return True
        return False