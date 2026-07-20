class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if nums[0] == 1:
            curr_max = 1
            maxx = 1
        else:
            curr_max = 0
            maxx = 0

        for i in range(1, len(nums)):
            if nums[i] == 1 and nums[i-1] == 1:
                curr_max += 1
            elif nums[i] == 1:
                curr_max = 1
            else:
                curr_max = 0

            maxx = max(maxx, curr_max)

        return maxx