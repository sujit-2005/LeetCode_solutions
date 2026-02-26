class Solution:
    def invert_substring(self, s, l, r):
        sub = s[l:r+1]
        inverted = sub.translate(str.maketrans('01', '10'))
        return s[:l] + inverted + s[r+1:]

    def minimumCost(self, s: str) -> int:
        count = 0
        n = len(s)
        mid = n // 2
        slow = 0
        while slow < n - 1:
            fast = slow + 1
            if s[slow] != s[fast]:
                if slow < mid:
                    # flip prefix
                    s = self.invert_substring(s, 0, slow)
                    count += (slow + 1)
                else:
                    # flip suffix
                    s = self.invert_substring(s, fast, n - 1)
                    count += (n - fast)
            slow += 1

        return count