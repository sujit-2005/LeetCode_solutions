class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for num,f in freq.items():
            if f > len(nums)//2:
                return num