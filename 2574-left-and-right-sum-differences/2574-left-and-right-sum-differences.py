class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum=0
        tot=sum(nums)
        d=[]
        for i in range(len(nums)):
            d.append(abs(leftsum-(tot-nums[i]-leftsum)))
            leftsum+=nums[i]
        return d