class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for num in freq:
            if freq[num]==1:
                return num
        