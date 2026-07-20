class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=[]
        for i in range(0,n):
            l.append(nums[nums[i]])
        return l