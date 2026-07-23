class Solution:
    def sortColors(self, nums: List[int]) -> None:
        slow = 0

        # First pass: move all 0s to the front
        for fast in range(len(nums)):
            if nums[fast] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

        # Second pass: move all 1s after the 0s
        for fast in range(slow, len(nums)):
            if nums[fast] == 1:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1