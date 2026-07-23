class Solution:
   def findDuplicate(self, nums: List[int]) -> int:
        mem=[False]*len(nums)
        for i in nums:
            if mem[i]:
                return i
            mem[i]=True