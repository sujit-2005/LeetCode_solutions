class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window=0
        for i in range(k):
            if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
                window+=1
            ans=window
        for j in range(k,len(s)):
            window+=1 if s[j]=="a" or s[j]=="e" or s[j]=="i" or s[j]=="o" or s[j]=="u" else 0
            window-=1 if s[j-k]=="a" or s[j-k]=="e" or s[j-k]=="i" or s[j-k]=="o" or s[j-k]=="u" else 0
            ans =max(window,ans)
        return ans
