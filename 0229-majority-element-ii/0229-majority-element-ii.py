class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        l=[]
        for num, f in freq.items():
            if f>len(nums)//3:
                l.append(num)
        return l