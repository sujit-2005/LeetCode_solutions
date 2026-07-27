class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        tot=sum(nums)
        leftsum=0
        for i in range(len(nums)):
            if leftsum==tot-nums[i]-leftsum:
                return i
            leftsum+=nums[i]
        return -1