class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        a = nums[:-1]
        b = nums[1:]

        d1 = [0] * (n - 1)
        d2 = [0] * (n - 1)

        d1[0] = a[0]
        d1[1] = max(a[0], a[1])

        d2[0] = b[0]
        d2[1] = max(b[0], b[1])

        for i in range(2, n - 1):
            d1[i] = max(d1[i-1], a[i] + d1[i-2])

        for i in range(2, n - 1):
            d2[i] = max(d2[i-1], b[i] + d2[i-2])

        return max(d1[-1], d2[-1])