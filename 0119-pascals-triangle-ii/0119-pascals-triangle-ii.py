class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex==1:
            return [1,1]
        prevRows = self.getRow(rowIndex - 1)
        newRow = [1] * (rowIndex+1)
        for i in range(1, rowIndex):
            newRow[i] = prevRows[i - 1] + prevRows[i]
        return newRow