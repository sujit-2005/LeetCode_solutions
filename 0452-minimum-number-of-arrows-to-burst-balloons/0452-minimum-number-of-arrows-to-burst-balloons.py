class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        print(points)
        count=0
        ends=None
        for start,end in points:
            if ends is not None and ends>=start:
                continue
            else:
                ends=end
                count+=1
        return count
