from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()

        left = 0
        ans = ""
        formed = 0
        required = len(need)

        for right in range(len(s)):
            ch = s[right]
            window[ch] += 1

            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:
                curr = s[left:right + 1]

                if ans == "" or len(curr) < len(ans):
                    ans = curr

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    formed -= 1

                left += 1

        return ans