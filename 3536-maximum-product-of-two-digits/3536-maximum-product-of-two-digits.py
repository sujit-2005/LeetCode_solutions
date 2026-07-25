class Solution:
    def maxProduct(self, n: int) -> int:
        s = str(n)

        first = 0
        second = 0

        for ch in s:
            digit = int(ch)

            if digit > first:
                second = first
                first = digit
            elif digit > second:
                second = digit

        return first * second