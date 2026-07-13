class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxx = max(nums)

        points = [0] * (maxx + 1)

        for num in nums:
            points[num] += num

        points = points[1:]

        if len(points) == 1:
            return points[0]

        d = [0] * len(points)

        d[0] = points[0]
        d[1] = max(points[0], points[1])

        for i in range(2, len(points)):
            d[i] = max(d[i - 1], points[i] + d[i - 2])

        return d[-1]