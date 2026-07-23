class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        equal = []
        right = []

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                right.append(num)

        return left + equal + right