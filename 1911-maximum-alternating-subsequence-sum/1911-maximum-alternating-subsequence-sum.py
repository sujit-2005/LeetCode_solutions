class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        even = 0
        odd = 0

        for num in nums:
            new_even = max(even, odd + num)
            new_odd = max(odd, even - num)

            even = new_even
            odd = new_odd

        return even