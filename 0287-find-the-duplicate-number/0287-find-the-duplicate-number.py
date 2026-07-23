class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        for n in d:
            if d[n]>1:
                return n