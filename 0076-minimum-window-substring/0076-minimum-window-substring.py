from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()

        left = 0
        ans = ""

        for right in range(len(s)):
            window[s[right]] += 1

            while all(window[ch] >= need[ch] for ch in need):
                if ans == "" or (right - left + 1) < len(ans):
                    ans = s[left:right+1]

                window[s[left]] -= 1
                left += 1

        return ans