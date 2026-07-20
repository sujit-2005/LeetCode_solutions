class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        freq1=set()
        for f in freq.values():
            if f in freq1:
                return False
            else:
                freq1.add(f)
        return True