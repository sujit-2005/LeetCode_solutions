class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        d=[]
        for num in nums:
            a=(num)**2
            d.append(a)
        d.sort()
        return d