class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        d=[0]*n
        l=0
        r=n-1
        pos=n-1
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                d[pos]=nums[l]**2
                l+=1
            else:
                d[pos]=nums[r]**2
                r-=1
            pos-=1
        return d