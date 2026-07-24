class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n=len(s)
        arr=[n]*n
        prev=-n
        for i in range (n):
            if s[i]==c:
                prev=i
            arr[i]=i-prev
        #print(arr)
        prev=2*n
        for i in range(n-1,-1,-1):
            if s[i]==c:
                prev=i
            arr[i]=min(arr[i],prev-i)
        return(arr)