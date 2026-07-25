class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        left=0
        min_length = float('inf')
        window=0
        for right in range(n):
            window+=nums[right]
            if window<target:
                continue
            while window>=target:
                min_length=min(min_length,right+1-left)
                window-=nums[left]
                left+=1
            if window==target:
                min_length=min(min_length,right+1-left)
        return 0 if min_length == float('inf') else min_length
