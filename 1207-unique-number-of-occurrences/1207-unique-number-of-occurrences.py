class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        freq1={}
        for f in freq.values():
            if f in freq1:
                freq1[f]+=1
            else:
                freq1[f]=1
        for ff in freq1.values():
            if ff!=1:
                return False
        return True