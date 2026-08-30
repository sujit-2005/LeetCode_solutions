class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last={}
        for i, ch in enumerate(s):
            last[ch]=i
        start=0
        end=0
        ans=[]
        for i,ch in enumerate(s):
            end=max(end,last[ch])
            if i==end:
                ans.append(i-start+1)
                start=i+1
        return ans