class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window=0
        for i in range (k):
            window+=nums[i]
        answer=window/k
        for j in range(k,len(nums)):
            window+=nums[j]
            window-=nums[j-k]
            answer=max(answer,window/k)
        return answer
