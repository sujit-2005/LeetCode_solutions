class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        ans.append(nums[0])
        n=len(nums)
        for i in range(1,n):
            ans.append(ans[i-1]+nums[i])
        return ans