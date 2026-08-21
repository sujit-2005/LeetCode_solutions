class Solution(object):
    def convertToTitle(self, columnNumber):
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        return ''.join(result[::-1])