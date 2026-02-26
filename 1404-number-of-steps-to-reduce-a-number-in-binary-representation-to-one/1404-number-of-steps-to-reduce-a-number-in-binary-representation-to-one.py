class Solution:
    def numSteps(self, s: str) -> int:
        count=0
        a=int(s,2)
        while a!=1:
            if a%2==0:
                a=a//2
            else:
                a+=1
            count+=1
        return count