class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows=0
        count=0
        while count<=n:
            count+=(rows+1)
            if count<=n:
                rows+=1
            else:
                return rows 