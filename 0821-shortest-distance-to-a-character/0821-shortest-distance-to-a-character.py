class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n=len(s)
        d=[0]*n
        for i in range(n):
            j=i
            lc=len(s)
            rc=len(s)
            while j>=0:
                if s[j]==c:
                    lc=min(lc,i-j)
                j-=1
            j=i
            while j<n:
                if s[j]==c:
                    rc=min(rc,j-i)
                j+=1
            d[i]=min(rc,lc)
        return d

        
